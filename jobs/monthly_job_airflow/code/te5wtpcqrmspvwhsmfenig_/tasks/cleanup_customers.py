def cleanup_customers():
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "cleanup_customers",
        json = {
          "task_key": "cleanup_customers", 
          "new_cluster": {
            "node_type_id": "i3.xlarge", 
            "spark_version": "12.2.x-scala2.12", 
            "runtime_engine": "STANDARD", 
            "num_workers": 0.0, 
            "data_security_mode": "SINGLE_USER", 
            "custom_tags": {"ResourceClass" : "SingleNode"}, 
            "spark_conf": {
              "spark.prophecy.metadata.job.uri": "__PROJECT_ID_PLACEHOLDER__/jobs/monthly_job_airflow", 
              "spark.prophecy.metadata.is.interactive.run": "false", 
              "spark.prophecy.metadata.fabric.id": "7627", 
              "spark.prophecy.tasks": "{\"ingest_customers\":\"pipelines/ingest_customers\",\"cleanup_orders\":\"pipelines/cleanup_orders\",\"mrr_reporting\":\"pipelines/mrr_reporting\",\"cleanup_customers\":\"pipelines/cleanup_customers\"}", 
              "spark.prophecy.metadata.url": "__PROPHECY_URL_PLACEHOLDER__", 
              "spark.master": "local[*, 4]", 
              "spark.prophecy.project.id": "__PROJECT_ID_PLACEHOLDER__", 
              "spark.prophecy.execution.metrics.disabled": False, 
              "spark.prophecy.metadata.job.branch": "__PROJECT_RELEASE_VERSION_PLACEHOLDER__", 
              "spark.databricks.cluster.profile": "singleNode", 
              "spark.prophecy.execution.service.url": "wss://execution.dp.app.prophecy.io/eventws"
            }, 
            "aws_attributes": {
              "first_on_demand": 1.0, 
              "availability": "SPOT_WITH_FALLBACK", 
              "zone_id": "auto", 
              "spot_bid_price_percent": 100.0
            }, 
            "spark_env_vars": {"PYSPARK_PYTHON" : "/databricks/python3/bin/python3"}, 
            "enable_elastic_disk": False
          }, 
          "python_wheel_task": {
            "package_name": "cleanup_customers", 
            "entry_point": "main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.1.53"}},                          {"pypi" : {"package" : "prophecy-libs==1.7.4"}},                          {
                           "whl": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/cleanup_customers-1.0-py3-none-any.whl"
                         }]
        },
        databricks_conn_id = "databricks-guides-dev",
    )
