from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingest_orders.config.ConfigStore import *
from ingest_orders.udfs.UDFs import *

def raw_orders(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/databricks-datasets/tpch/delta-001/orders/")
