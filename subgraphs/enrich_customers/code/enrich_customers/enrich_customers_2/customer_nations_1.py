from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def customer_nations_1(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/databricks-datasets/tpch/delta-001/customer/")
