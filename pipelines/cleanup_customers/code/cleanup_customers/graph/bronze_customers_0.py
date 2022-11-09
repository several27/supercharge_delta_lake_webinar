from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from cleanup_customers.config.ConfigStore import *
from cleanup_customers.udfs.UDFs import *

def bronze_customers_0(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/databricks-datasets/tpch/delta-001/customer/")
