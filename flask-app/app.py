from flask import Flask
from prometheus_client import start_http_server, Gauge, generate_latest
import random
import time
import threading

app = Flask(__name__)

# Prometheus metrics
cpu_usage_gauge = Gauge('flask_app_cpu_usage', 'CPU usage of Flask app')
memory_usage_gauge = Gauge('flask_app_memory_usage', 'Memory usage of Flask app')
up_gauge = Gauge('up', 'Health status of Flask app')

# Simulate metrics
def generate_metrics():
    while True:
        cpu_usage = random.uniform(10, 100)  # Simulated CPU usage (10% to 100%)
        memory_usage = random.uniform(10, 100)  # Simulated Memory usage (10% to 100%)
        
        cpu_usage_gauge.set(cpu_usage)
        memory_usage_gauge.set(memory_usage)
        up_gauge.set(1)  # Flask app is up
        
        time.sleep(15)  # Update every 15 seconds


# Background thread for generating metrics
thread = threading.Thread(target=generate_metrics)
thread.daemon = True
thread.start()

@app.route('/')
def home():
    return "Flask App Metrics Available at /metrics"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}
    # return "test"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
