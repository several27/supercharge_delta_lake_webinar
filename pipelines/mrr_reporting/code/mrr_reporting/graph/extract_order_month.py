from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def extract_order_month(spark: SparkSession, by_customer_id: DataFrame) -> DataFrame:
    return by_customer_id.select(
        month(to_date(col("o_orderdate"))).alias("month"), 
        col("c_custkey"), 
        col("c_name"), 
        col("c_address"), 
        col("c_nationkey"), 
        col("c_phone"), 
        col("c_acctbal"), 
        col("c_mktsegment"), 
        col("c_comment"), 
        col("o_orderkey"), 
        col("o_custkey"), 
        col("o_orderstatus"), 
        col("o_totalprice"), 
        col("o_orderdate"), 
        col("o_orderpriority"), 
        col("o_clerk"), 
        col("o_shippriority"), 
        col("o_comment")
    )
