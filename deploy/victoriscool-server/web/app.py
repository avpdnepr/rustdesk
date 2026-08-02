import asyncio
import base64
import hmac
import os
from pathlib import Path
from typing import Dict

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import FileResponse, JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

SERVER_HOST = os.getenv("SERVER_HOST", "217.24.161.103")
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
WEB_PORT = int(os.getenv("WEB_PORT", "8080"))
PUBLIC_KEY_FILE = Path("/data/id_ed25519.pub")

security = HTTPBasic()
app = FastAPI(title="VictorIsCool Server", docs_url=None, redoc_url=None)


def require_auth(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    user_ok = hmac.compare_digest(credentials.username.encode(), ADMIN_USER.encode())
    password_ok = hmac.compare_digest(credentials.password.encode(), ADMIN_PASSWORD.encode())
    if not (user_ok and password_ok and ADMIN_PASSWORD):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


async def tcp_probe(host: str, port: int, timeout: float = 1.0) -> bool:
    try:
        _, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout)
        writer.close()
        await writer.wait_closed()
        return True
    except Exception:
        return False


def public_key() -> str:
    try:
        key = PUBLIC_KEY_FILE.read_text(encoding="utf-8").strip()
        if len(base64.b64decode(key, validate=True)) != 32:
            raise ValueError("Unexpected public key length")
        return key
    except Exception:
        return ""


@app.get("/")
async def index(_: str = Depends(require_auth)):
    return FileResponse("/app/static/index.html")


@app.get("/api/status")
async def api_status(_: str = Depends(require_auth)) -> Dict[str, object]:
    ports = {
        "hbbs_nat_test_tcp": 21115,
        "hbbs_id_tcp": 21116,
        "hbbr_relay_tcp": 21117,
        "hbbs_websocket_tcp": 21118,
        "hbbr_websocket_tcp": 21119,
    }
    results = await asyncio.gather(*(tcp_probe(SERVER_HOST, port) for port in ports.values()))
    return {
        "product": "VictorIsCool",
        "server": SERVER_HOST,
        "services": {
            name: {"port": port, "online": online}
            for (name, port), online in zip(ports.items(), results)
        },
        "public_key_present": bool(public_key()),
    }


@app.get("/api/config")
async def api_config(_: str = Depends(require_auth)):
    payload = {
        "product_name": "VictorIsCool",
        "id_server": SERVER_HOST,
        "relay_server": SERVER_HOST,
        "key": public_key(),
        "languages": ["de", "en", "uk"],
        "default_language": "uk",
    }
    return JSONResponse(
        payload,
        headers={"Content-Disposition": 'attachment; filename="victoriscool-client-config.json"'},
    )


@app.get("/api/key")
async def api_key(_: str = Depends(require_auth)):
    key = public_key()
    if not key:
        raise HTTPException(status_code=503, detail="Public key is unavailable")
    return {"public_key": key}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=WEB_PORT, proxy_headers=True)
