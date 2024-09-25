from te5wtpcqrmspvwhsmfenig_.utils import *

@task_wrapper(task_id = "ingest_customers")
def ingest_customers(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "ingest_customers",
        json = {
          "task_key": "ingest_customers", 
          "new_cluster": {
            "node_type_id": "i3.xlarge", 
            "spark_version": "11.3.x-scala2.12", 
            "num_workers": 1.0, 
            "spark_conf": {
              "spark.prophecy.execution.metrics.component-metrics.table": "main.maciej.prophecy_component_runs", 
              "spark.prophecy.metadata.job.uri": "__PROJECT_ID_PLACEHOLDER__/jobs/monthly_job_airflow", 
              "spark.prophecy.execution.metrics.interims.table": "main.maciej.prophecy_interims", 
              "spark.prophecy.metadata.is.interactive.run": "false", 
              "spark.prophecy.metadata.fabric.id": "1618", 
              "spark.prophecy.tasks": "H4sIAAAAAAAAAKuuBQBDv6ajAgAAAA==", 
              "spark.prophecy.metadata.url": "__PROPHECY_URL_PLACEHOLDER__", 
              "spark.prophecy.metadata.user.id": "6", 
              "spark.prophecy.execution.metrics.pipeline-metrics.table": "main.maciej.prophecy_pipeline_runs", 
              "spark.prophecy.project.id": "__PROJECT_ID_PLACEHOLDER__", 
              "spark.prophecy.execution.metrics.disabled": "false", 
              "spark.databricks.isv.product": "prophecy", 
              "spark.prophecy.metadata.job.branch": "__PROJECT_RELEASE_VERSION_PLACEHOLDER__", 
              "spark.prophecy.execution.service.url": "wss://execution.dp.app.prophecy.io/eventws"
            }, 
            "driver_node_type_id": "i3.xlarge"
          }, 
          "python_wheel_task": {
            "package_name": "ingest_customers", 
            "entry_point": "main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-8.0.31"}},                          {"pypi" : {"package" : "prophecy-libs==1.9.9"}},                          {
                           "whl": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/ingest_customers-1.0-py3-none-any.whl"
                         }]
        },
        databricks_conn_id = "",
    )
