from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.functions import *

@instrument
def by_c_custkey_c_comment(spark: SparkSession, silver_customers: DataFrame, silver_orders: DataFrame, ) -> DataFrame:
    return silver_customers\
        .alias("silver_customers")\
        .join(
          silver_orders.alias("silver_orders"),
          (col("silver_customers.c_custkey") == col("silver_orders.o_custkey")),
          "inner"
        )\
        .select(col("silver_orders.o_orderkey").alias("o_orderkey"), col("silver_orders.o_orderstatus").alias("o_orderstatus"), col("silver_orders.o_totalprice").alias("o_totalprice"), col("silver_orders.o_orderdate").alias("o_orderdate"), col("silver_orders.o_orderpriority").alias("o_orderpriority"), col("silver_orders.o_clerk").alias("o_clerk"), col("silver_orders.o_shippriority").alias("o_shippriority"), col("silver_customers.c_phone").alias("c_phone"), col("silver_customers.c_custkey").alias("c_custkey"), col("silver_customers.c_comment").alias("c_comment"), col("silver_customers.c_mktsegment").alias("c_mktsegment"), col("silver_customers.c_address").alias("c_address"), col("silver_customers.c_nationkey").alias("c_nationkey"), col("silver_customers.c_name").alias("c_name"), col("silver_customers.c_acctbal").alias("c_acctbal"))
