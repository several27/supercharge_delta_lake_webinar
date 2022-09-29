from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gold_mrr.config.ConfigStore import *
from gold_mrr.udfs.UDFs import *

def silver_orders_0(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"lakehouse.silver_orders")
