from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingest_customers.config.ConfigStore import *
from ingest_customers.udfs.UDFs import *

def raw_customers(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/databricks-datasets/tpch/delta-001/customer/")
