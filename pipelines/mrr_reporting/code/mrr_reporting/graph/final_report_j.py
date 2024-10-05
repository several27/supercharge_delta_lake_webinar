from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.functions import *

@instrument
def final_report_j(spark: SparkSession, enrich_customers: DataFrame):
    enrich_customers.write.format("delta").mode("overwrite").saveAsTable("`lakehouse`.`final_report_2`")
