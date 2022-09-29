from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingest_customers.config.ConfigStore import *
from ingest_customers.udfs.UDFs import *

def bronze_customers_1(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder
    in0.write.format("delta").mode("overwrite").save("dbfs:/Prophecy/maciej+webinar-2022@prophecy.io/bronze_customers/")
