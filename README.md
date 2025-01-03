# Notification grouping

This repository demonstrates how to use Prometheus and Grafana to showcase **alert notification grouping**. It is a summarized version of the Grafana tutorial [Get started with Grafana Alerting - Part 3](https://grafana.com/tutorials/alerting-get-started-pt3/). For more details, visit the full tutorial

### Prometheus
Prometheus is configured to scrape metrics from services running in Docker containers. The metric `up` is particularly useful in this demo:

- `up{}` indicates whether a target is up (`1`) or down (`0`).

You can also leverage key-value pairs such as `job` and `instance` to group metrics by a specific service or target within a job:

  - `job`: The monitored job or service (e.g., `flask`, `nginx`.).
  - `instance`: The instance of the service (e.g., `localhost:5000`, `localhost:8081`).

For instance, by querying `up{} == 0`, we can detect when targets go down and use their labels to route alert instances.

### Grafana Alerting

Alert notifications can be grouped and routed dinamically:

- **Grouping:** Consolidates multiple alerts into fewer notifications by grouping based on specific labels (e.g., `job`, `instance`).
- **Routing:** Dynamically routes notifications to specific contact points based on label matchers (e.g., `team`).

---

## Demonstrating grouping

### Step 1. Trigger alert rules
1. **Shutting down services**:
   - Stop one or more Docker containers.
   - Prometheus will detect the targets as `down` (`up == 0`), triggering alerts in Grafana.

   ```bash
   docker stop flask
   ```

2. **Restarting services**:
   - Restart the stopped containers to resolve the alerts.

   ```bash
   docker start flask
   ```

### Step 2. View alert notifications without grouping
Without grouping, each alert generates a separate notification. For example:

- **Alert notification 1:** Instance `localhost:5000` of job `flask-app` is down.
- **Alert notification 2:** Instance `localhost:8001` of job `nginx` is down.

This can overwhelm the on-call team with redundant notifications.

### Step 3. Enable grouping
Enable grouping in Grafana to consolidate alert notifications based on specific labels. Examples:

In the **Notification policy**:

- **Group by `job`:**
  - This would output a single notification informing that multiple instances of job `flask-app`, or `nginx` are down.

- **Group by `instance`:**
  - Receive separate notifications for each instance, but consolidated within their group.

### Step 4: Routing with label matchers
Use additional labels from the `up` metric to route alerts dynamically. Examples:

- **Label: `team`**:
  - Alert instances from `job=flask-app` route to the Flask team.
  - Alert instances from `job=nginx` route to Web Services team.

- **Label: `instance`**:
  - Alert instances from `instance=localhost:5000` (flask), `instance=localhost:8081` (nginx) route to a specific contact point.


Use these metrics to create new alert rules and benefit from grouping based on different labels.
