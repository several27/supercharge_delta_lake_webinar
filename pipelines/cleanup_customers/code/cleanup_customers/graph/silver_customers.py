from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from cleanup_customers.config.ConfigStore import *
from cleanup_customers.udfs import *

@instrument
def silver_customers(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`lakehouse`.`silver_customers`")
