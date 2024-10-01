from airflow.decorators import task

db_pipeline_id_to_path_dict = {
    "pipelines/cleanup_customers": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/cleanup_customers-1.0-py3-none-any.whl", 
    "pipelines/cleanup_orders": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/cleanup_orders-1.0-py3-none-any.whl", 
    "pipelines/ingest_customers": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/ingest_customers-1.0-py3-none-any.whl", 
    "pipelines/ingest_orders": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/ingest_orders-1.0-py3-none-any.whl", 
    "pipelines/mrr_reporting": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/mrr_reporting-1.0-py3-none-any.whl"
}


def task_wrapper(task_id):

    def decorator(func):

        @task(task_id = task_id)
        def wrapper(*args, **context):
            ## running the actual method.
            return func(*args, **context).execute(context)

        return wrapper

    return decorator

pipeline_package_name = {
    "pipelines/ingest_customers": "ingest_customers", 
    "pipelines/ingest_orders": "ingest_orders", 
    "pipelines/cleanup_customers": "cleanup_customers", 
    "pipelines/mrr_reporting": "mrr_reporting", 
    "pipelines/cleanup_orders": "cleanup_orders"
}
