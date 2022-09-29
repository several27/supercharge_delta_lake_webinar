from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from cleanup_customers.config.ConfigStore import *
from cleanup_customers.udfs.UDFs import *

def silver_customers(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder
    in0.write.format("delta").mode("overwrite").save("dbfs:/Prophecy/maciej+webinar-2022@prophecy.io/silver_customers/")
