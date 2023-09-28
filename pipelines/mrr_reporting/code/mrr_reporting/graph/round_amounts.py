from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def round_amounts(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("c_custkey"), col("month"), floor(col("amounts")).alias("amounts"))
