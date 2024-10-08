from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.functions import *

@instrument
def silver_orders(spark: SparkSession) -> DataFrame:
    return spark.read.table("`lakehouse`.`silver_orders`")
