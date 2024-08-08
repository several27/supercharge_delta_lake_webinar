from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

@instrument
def reformatted_silver_customers(spark: SparkSession, silver_customers_2_1: DataFrame) -> DataFrame:
    return silver_customers_2_1.select(
        col("customer_id"), 
        col("first_name"), 
        col("last_name"), 
        col("first_order"), 
        col("most_recent_order"), 
        col("total_orders"), 
        col("customer_lifetime_value")
    )
