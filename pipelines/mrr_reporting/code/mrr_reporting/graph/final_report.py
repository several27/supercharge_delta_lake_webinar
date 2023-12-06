from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def final_report(spark: SparkSession, in0: DataFrame):
    from pyspark.sql.utils import AnalysisException

    try:
        desc_table = spark.sql("describe formatted `lakehouse`.`final_report`")
        table_exists = True
    except AnalysisException as e:
        table_exists = False

    in0.write.format("delta").mode("error").saveAsTable("`lakehouse`.`final_report`")
