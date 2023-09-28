from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from cleanup_orders.config.ConfigStore import *
from cleanup_orders.udfs.UDFs import *

def bronze_orders(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"lakehouse.bronze_orders")
