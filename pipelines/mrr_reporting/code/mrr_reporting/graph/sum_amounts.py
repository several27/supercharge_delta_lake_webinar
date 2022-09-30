from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def sum_amounts(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(month(col("o_orderdate")).alias("month"), col("c_custkey"))

    return df1.agg(sum(col("o_totalprice")).alias("amounts"))
