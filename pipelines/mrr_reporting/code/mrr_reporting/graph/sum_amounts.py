from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def sum_amounts(spark: SparkSession, by_customer_id: DataFrame) -> DataFrame:
    df1 = by_customer_id.groupBy(col("c_custkey"), month(col("o_orderdate")).alias("month"))

    return df1.agg(sum(col("o_totalprice")).alias("amounts"))
