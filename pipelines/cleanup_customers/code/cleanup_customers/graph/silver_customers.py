from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from cleanup_customers.config.ConfigStore import *
from cleanup_customers.udfs.UDFs import *

def silver_customers(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("error").saveAsTable(f"lakehouse.silver_customers")
