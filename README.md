# Monitoring with Prometheus and Grafana: metrics, visualization, and alert rules

This repository contains the files for the [Alerting - Link alerts to visualizations tutorial](https://grafana.com/tutorials/alerting-get-started-pt6/). It provides a practical guide to setting up monitoring with Prometheus and Grafana. This fully dockerized solution eliminates the need for manual setup, allowing you to quickly spin up a pre-configured environment. Learn how to collect simulated metrics, visualize them in Grafana, and configure alert rules to track anomalies and system health.



## Set up the Grafana stack

Clone the tutorial environment repository.
```
git clone https://github.com/tonypowa/grafana-prometheus-alerting-demo.git
```

Change to the directory where you cloned the repository:
```
cd grafana-prometheus-alerting-demo
```

Build the Grafana stack:
```
docker compose build
```

Bring up the containers:

```
docker compose up –d
```

![image](https://github.com/user-attachments/assets/b1de32ea-b960-4601-a2f5-35a67f3bec7a)


