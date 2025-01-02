from flask import Flask
from prometheus_client import start_http_server, Summary, generate_latest

# Create Flask app
app = Flask(__name__)

# Create a metric to track request latency
REQUEST_LATENCY = Summary('request_latency_seconds', 'Request latency in seconds')

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/metrics')
@REQUEST_LATENCY.time()
def metrics():
    return generate_latest() # formats the metrics into a text format that Prometheus can scrape

if __name__ == '__main__':
    # Start Prometheus metrics server
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
