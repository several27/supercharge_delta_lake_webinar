def cleanup_customers():
    settings = {}
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "cleanup_customers",
        json = {
          "task_key": "cleanup_customers", 
          "new_cluster": {
            "node_type_id": "i3.xlarge", 
            "spark_version": "11.3.x-scala2.12", 
            "num_workers": 1, 
            "spark_conf": {
              "spark.prophecy.metadata.job.uri": "__PROJECT_ID_PLACEHOLDER__/jobs/monthly_job_airflow", 
              "spark.prophecy.metadata.is.interactive.run": "false", 
              "spark.prophecy.metadata.fabric.id": "3346", 
              "spark.prophecy.metadata.url": "__PROPHECY_URL_PLACEHOLDER__", 
              "spark.prophecy.packages.path": "{\"pipelines/ingest_customers\":\"dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/ingest_customers-1.0-py3-none-any.whl\",\"pipelines/cleanup_orders\":\"dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/cleanup_orders-1.0-py3-none-any.whl\",\"pipelines/mrr_reporting\":\"dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/mrr_reporting-1.0-py3-none-any.whl\",\"pipelines/cleanup_customers\":\"dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/cleanup_customers-1.0-py3-none-any.whl\"}", 
              "spark.prophecy.project.id": "__PROJECT_ID_PLACEHOLDER__", 
              "spark.prophecy.execution.metrics.disabled": False, 
              "spark.databricks.isv.product": "prophecy", 
              "spark.prophecy.metadata.job.branch": "__PROJECT_RELEASE_VERSION_PLACEHOLDER__", 
              "spark.prophecy.execution.service.url": "wss://execution.dp.app.prophecy.io/eventws"
            }, 
            "driver_node_type_id": "i3.xlarge"
          }, 
          "python_wheel_task": {
            "package_name": "cleanup_customers", 
            "entry_point": "main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.1.15"}},                          {"pypi" : {"package" : "prophecy-libs==1.6.2"}},                          {
                           "whl": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/cleanup_customers-1.0-py3-none-any.whl"
                         }]
        },
        databricks_conn_id = "4npOWsozwwNgHSZRCjEQ1",
        **settings
    )
