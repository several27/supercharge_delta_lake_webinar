from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from mrr_reporting.udfs.UDFs import *

def nation_1(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/databricks-datasets/tpch/delta-001/nation/")
