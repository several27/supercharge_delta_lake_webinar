import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from te5wtpcqrmspvwhsmfenig_.tasks import cleanup_customers, cleanup_orders, ingest_customers, mrr_reporting
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "tE5wTpcqrmsPVWhsmfENIg_", 
    schedule_interval = "0 0 1 * *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "KWdUsXmL"}, 
    start_date = pendulum.datetime(2023, 8, 3, tz = "UTC"), 
    end_date = pendulum.datetime(2023, 8, 4, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    ingest_customers_op = ingest_customers()
    cleanup_orders_op = cleanup_orders()
    mrr_reporting_op = mrr_reporting()
    cleanup_customers_op = cleanup_customers()
    ingest_customers_op >> cleanup_customers_op
    [cleanup_customers_op, cleanup_orders_op] >> mrr_reporting_op
