from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from cleanup_customers.config.ConfigStore import *
from cleanup_customers.udfs import *

@instrument
def bronze_customers_0(spark: SparkSession) -> DataFrame:
    return spark.read.table("`lakehouse`.`bronze_customers`")
