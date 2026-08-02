FROM python:3.13-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY static ./static
RUN adduser -D -H -u 10001 app
USER app
CMD ["python", "/app/app.py"]
