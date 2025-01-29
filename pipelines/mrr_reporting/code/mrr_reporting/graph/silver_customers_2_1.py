from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs import *

def silver_customers_2_1(spark: SparkSession) -> DataFrame:
    return spark.read.table("`lakehouse`.`silver_customers`")
