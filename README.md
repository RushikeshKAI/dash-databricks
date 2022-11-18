# dash-databricks
Build Real-Time Production Data Apps with Databricks &amp; Plotly Dash. We used the Databricks SQL connector for Python (DB SQL) within a Plotly Dash app to run queries on Databricks SQL endpoints, demonstrating the efficacy of this method for managing data-warehousing style workloads with high concurrency and low latency SLAs.

# Introduction
Dash was designed to be a stateless framework.

Stateless frameworks are more scalable and robust than stateful ones. Most websites that you visit are running on stateless servers.

They are more scalable because it's trivial to add more compute power to the application. In order to scale the application to serve more users or run more computations, run more "copies" of the app in separate processes.

