from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_day.config.ConfigStore import *
from demo_day.udfs.UDFs import *

def final_table(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable(f"lakehouse.final_table")
