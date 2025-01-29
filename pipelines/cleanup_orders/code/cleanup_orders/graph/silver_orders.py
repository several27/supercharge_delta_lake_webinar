from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from cleanup_orders.config.ConfigStore import *
from cleanup_orders.udfs import *

def silver_orders(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("error").saveAsTable("`lakehouse`.`silver_orders`")
