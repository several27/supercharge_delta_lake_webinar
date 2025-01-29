from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.functions import *

@instrument
def reformat_order_customer_data(spark: SparkSession, by_c_custkey_c_comment: DataFrame) -> DataFrame:
    return by_c_custkey_c_comment.select(
        month(to_date(col("o_orderdate"))).alias("month"), 
        col("o_orderkey"), 
        col("o_orderstatus"), 
        col("o_totalprice"), 
        col("o_orderdate"), 
        col("o_orderpriority"), 
        col("o_clerk"), 
        col("o_shippriority"), 
        col("c_phone"), 
        col("c_custkey"), 
        col("c_comment"), 
        col("c_mktsegment"), 
        col("c_address"), 
        col("c_nationkey"), 
        col("c_name"), 
        col("c_acctbal")
    )
