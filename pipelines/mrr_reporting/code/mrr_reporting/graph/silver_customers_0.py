from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def silver_customers_0(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"lakehouse.silver_customers")
