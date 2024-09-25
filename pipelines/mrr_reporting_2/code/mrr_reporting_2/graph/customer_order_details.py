from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting_2.config.ConfigStore import *
from mrr_reporting_2.functions import *

def customer_order_details(spark: SparkSession, bronze_customers: DataFrame, bronze_orders: DataFrame, ) -> DataFrame:
    return bronze_customers\
        .alias("bronze_customers")\
        .join(
          bronze_orders.alias("bronze_orders"),
          (col("bronze_customers.c_custkey") == col("bronze_orders.o_custkey")),
          "inner"
        )\
        .select(col("bronze_customers.c_custkey").alias("C_CUSTKEY"), col("bronze_customers.c_name").alias("C_NAME"), col("bronze_orders.o_totalprice").alias("O_TOTALPRICE"))
