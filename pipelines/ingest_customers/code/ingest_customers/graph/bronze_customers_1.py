from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from ingest_customers.config.ConfigStore import *
from ingest_customers.udfs import *

@instrument
def bronze_customers_1(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`lakehouse`.`bronze_customers`")
