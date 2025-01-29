from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.functions import *

@instrument
def total_amount_by_month_and_customer(spark: SparkSession, reformat_order_customer_data: DataFrame) -> DataFrame:
    df1 = reformat_order_customer_data.groupBy(col("month"), col("c_custkey"))

    return df1.agg(sum(col("o_totalprice")).alias("amounts"))
