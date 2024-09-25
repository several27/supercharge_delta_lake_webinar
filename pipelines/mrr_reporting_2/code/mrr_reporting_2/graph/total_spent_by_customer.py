from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting_2.config.ConfigStore import *
from mrr_reporting_2.functions import *

def total_spent_by_customer(spark: SparkSession, customer_order_details: DataFrame) -> DataFrame:
    df1 = customer_order_details.groupBy(col("C_CUSTKEY"), col("C_NAME"))

    return df1.agg(sum(col("o_totalprice")).alias("TOTAL_SPENT"))
