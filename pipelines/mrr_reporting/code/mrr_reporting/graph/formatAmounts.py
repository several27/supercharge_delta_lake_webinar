from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def formatAmounts(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("c_custkey"), col("month"), format_number(col("amounts"), 2).alias("amounts"))
