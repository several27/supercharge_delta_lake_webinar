from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting_2.config.ConfigStore import *
from mrr_reporting_2.functions import *

def bronze_orders(spark: SparkSession) -> DataFrame:
    return spark.read.table("`lakehouse`.`bronze_orders`")
