from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, generate_latest


app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")

@app.route("/")
def helloworld():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
