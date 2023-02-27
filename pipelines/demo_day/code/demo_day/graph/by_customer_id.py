from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from demo_day.config.ConfigStore import *
from demo_day.udfs.UDFs import *

def by_customer_id(spark: SparkSession, silver_orders: DataFrame, in1: DataFrame, ) -> DataFrame:
    return silver_orders\
        .alias("silver_orders")\
        .join(in1.alias("in1"), (col("silver_orders.o_custkey") == col("in1.c_custkey")), "inner")
