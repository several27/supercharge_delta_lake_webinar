from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def sum_amounts_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("c_custkey"), month(col("o_orderdate")).alias("month"))

    return df1.agg(sum(col("o_totalprice")).alias("amounts"))
