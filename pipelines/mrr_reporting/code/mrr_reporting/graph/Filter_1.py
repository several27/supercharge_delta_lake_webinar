from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def Filter_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(lit(True))
