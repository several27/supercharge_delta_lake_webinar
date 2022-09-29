from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingest_orders.config.ConfigStore import *
from ingest_orders.udfs.UDFs import *

def bronze_orders(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("lakehouse.bronze_orders")
