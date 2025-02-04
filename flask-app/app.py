from flask import Flask
from prometheus_client import Gauge, generate_latest
import random
import time
import threading
import os

app = Flask(__name__)

# Determine environment based on container hostname
ENVIRONMENT = os.getenv("ENVIRONMENT", "staging")  # Default to 'staging' if not set

# Prometheus metrics with 'environment' label
cpu_usage_gauge = Gauge('flask_app_cpu_usage', 'CPU usage of Flask app', ['environment'])
memory_usage_gauge = Gauge('flask_app_memory_usage', 'Memory usage of Flask app', ['environment'])
up_gauge = Gauge('up', 'Health status of Flask app', ['environment'])

# Simulate metrics
def generate_metrics():
    while True:
        cpu_usage = random.uniform(10, 100)  # Simulated CPU usage (10% to 100%)
        memory_usage = random.uniform(10, 100)  # Simulated Memory usage (10% to 100%)

        cpu_usage_gauge.labels(environment=ENVIRONMENT).set(cpu_usage)
        memory_usage_gauge.labels(environment=ENVIRONMENT).set(memory_usage)
        up_gauge.labels(environment=ENVIRONMENT).set(1)  # Flask app is up
        
        time.sleep(15)  # Update every 15 seconds

# Background thread for generating metrics
thread = threading.Thread(target=generate_metrics)
thread.daemon = True
thread.start()

@app.route('/')
def home():
    return f"Flask App Metrics Available at /metrics (Environment: {ENVIRONMENT})"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
