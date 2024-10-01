import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from supercharge_delta_lake_monthly.tasks import cleanup_customers, cleanup_orders, ingest_customers, mrr_reporting
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "supercharge_delta_lake_monthly", 
    schedule_interval = "0 0 1 * *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.datetime(2024, 11, 3, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    ingest_customers_op = ingest_customers()
    cleanup_orders_op = cleanup_orders()
    cleanup_customers_op = cleanup_customers()
    mrr_reporting_op = mrr_reporting()
    ingest_customers_op >> cleanup_customers_op
    [cleanup_customers_op, cleanup_orders_op] >> mrr_reporting_op
