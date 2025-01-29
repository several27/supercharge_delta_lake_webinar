from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from ingest_orders.config.ConfigStore import *
from ingest_orders.functions import *

@instrument
def bronze_orders(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`lakehouse`.`bronze_orders`")
