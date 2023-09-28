from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_day.config.ConfigStore import *
from demo_day.udfs.UDFs import *

def silver_customers(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"lakehouse.silver_customers")
