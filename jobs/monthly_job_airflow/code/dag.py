import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from te5wtpcqrmspvwhsmfenig_.tasks import DBT_1, cleanup_customers, cleanup_orders, ingest_customers, mrr_reporting
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
    DBT_1_op = DBT_1()
    ingest_customers_op = ingest_customers()
    cleanup_orders_op = cleanup_orders()
    cleanup_customers_op = cleanup_customers()
    mrr_reporting_op = mrr_reporting()
    ingest_customers_op >> cleanup_customers_op
    [cleanup_customers_op, cleanup_orders_op] >> mrr_reporting_op
