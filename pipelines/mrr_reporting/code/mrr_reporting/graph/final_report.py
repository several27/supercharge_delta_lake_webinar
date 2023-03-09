from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def final_report(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("error").saveAsTable(f"lakehouse.final_report")
