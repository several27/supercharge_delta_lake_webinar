from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from cleanup_orders.config.ConfigStore import *
from cleanup_orders.udfs.UDFs import *

def silver_orders(spark: SparkSession, in0: DataFrame):
    from pyspark.sql.utils import AnalysisException

    try:
        desc_table = spark.sql("describe formatted `lakehouse`.`silver_orders`")
        table_exists = True
    except AnalysisException as e:
        table_exists = False

    in0.write.format("delta").mode("error").saveAsTable("`lakehouse`.`silver_orders`")
