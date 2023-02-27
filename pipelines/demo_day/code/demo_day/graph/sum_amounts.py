from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from demo_day.config.ConfigStore import *
from demo_day.udfs.UDFs import *

def sum_amounts(spark: SparkSession, by_customer_id: DataFrame) -> DataFrame:
    df1 = by_customer_id.groupBy(col("c_custkey"), month(col("o_orderdate")).alias("month"))

    return df1.agg(sum(col("o_totalprice")).alias("amounts"))
