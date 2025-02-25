# Monitoring with Prometheus and Grafana: metrics, visualization, and alert rules

This repository contains the files for the [Get Started with Grafana Alerting - Part 5 tutorial](https://grafana.com/tutorials/alerting-get-started-pt5/). It provides a practical guide to setting up monitoring with Prometheus and Grafana. This fully dockerized solution eliminates the need for manual setup, allowing you to quickly spin up a pre-configured environment. Learn how to collect simulated metrics, visualize them in Grafana, and configure alert rules to track anomalies and system health.

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

## Configure alert rules, and visualize alert state in Grafana.

Grafana Alerting allows you to monitor critical metrics and create actionable notifications for your dashboards. Follow these steps to manually create alert rules and link them to the visualizations (available only in time series panels):

1. **Log in to Grafana**:
    - Navigate to http://localhost:3000, where Grafana should be running.
    - Username and password: `admin`
1. **Create a time series panel**  
   - In Grafana, create a new dashboard and add a time series panel.
   - Configure the panel to query CPU usage metrics using PromQL. For example:
     ```promql
     flask_app_cpu_usage{job="flask"}
     ```
   - This query will display the simulated CPU usage data as a time series graph.
   - Save your dashboard.

2. **Create an alert rule for CPU sage**  
   - Navigate to **Alerting** > **Alert rules** from the Grafana sidebar.
   - Click **New alert rule** to create a new alert.
   - In the alert rule configuration, enter the same query used in the time series panel (e.g., `flask_app_cpu_usage{job="flask"}`).
   - Define a condition to trigger the alert, such as CPU usage exceeding `80%`. For example:

     ![image](https://github.com/user-attachments/assets/5ef6bad8-bf09-469b-9fb9-8e877d7fc2b3)

3. **Link the alert rule to the panel**  
   - Scroll down to the Configure notification message section
   - Click **Link dashboard and panel**.
   - Find the panel that you created earlier.
   - Click **Confirm**
   - Complete any other additional required details.
   - Click **Save rule and exit**

4. **Repeat for memory usage**  
   
   - Create a new alert rule for memory usage, defining a threshold condition (e.g., memory usage exceeding `75%`).

Once the alert rules are created, they should appear as **health indicators** (colored heart icons: red heart when the alert is in Alerting state, and green heart when in Normal state..) on the linked panel.
In addition, the annotations will include helpful context, such as the time the alert was triggered.

![image](https://github.com/user-attachments/assets/b1de32ea-b960-4601-a2f5-35a67f3bec7a)


