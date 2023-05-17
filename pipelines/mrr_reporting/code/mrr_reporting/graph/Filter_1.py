from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def Filter_1(spark: SparkSession, Limit_1: DataFrame) -> DataFrame:
    return Limit_1.filter(lit(True))
