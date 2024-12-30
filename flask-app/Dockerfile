FROM python:3.9-slim

WORKDIR /app

RUN pip install flask prometheus_client

COPY app.py /app/

# Expose the application's port
EXPOSE 5000

CMD ["python", "app.py"]
