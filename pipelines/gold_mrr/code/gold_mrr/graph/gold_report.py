from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gold_mrr.config.ConfigStore import *
from gold_mrr.udfs.UDFs import *

def gold_report(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("lakehouse.gold_report")
