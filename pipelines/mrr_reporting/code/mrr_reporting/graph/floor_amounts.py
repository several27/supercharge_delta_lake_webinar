from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def floor_amounts(spark: SparkSession, sum_amounts: DataFrame) -> DataFrame:
    return sum_amounts.select(col("c_custkey"), col("month"), floor(col("amounts")).alias("amounts"))
