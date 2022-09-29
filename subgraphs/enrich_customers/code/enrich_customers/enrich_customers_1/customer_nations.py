from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from golde.config.ConfigStore import *
from golde.udfs.UDFs import *

def customer_nations(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/databricks-datasets/tpch/delta-001/customer/")
