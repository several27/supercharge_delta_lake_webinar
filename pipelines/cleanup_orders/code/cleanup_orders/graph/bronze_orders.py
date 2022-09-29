from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from cleanup_orders.config.ConfigStore import *
from cleanup_orders.udfs.UDFs import *

def bronze_orders(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/Prophecy/maciej+webinar-2022@prophecy.io/bronze_orders/")
