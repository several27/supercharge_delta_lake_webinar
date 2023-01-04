from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *

def customers_orders_1(spark: SparkSession) -> DataFrame:
    df_silvers_orders_1 = silvers_orders_1(spark)
    df_silver_customers_0_1 = silver_customers_0_1(spark)
    df_by_customer_id_1 = by_customer_id_1(spark, df_silver_customers_0_1, df_silvers_orders_1)
    df_sum_amounts_1 = sum_amounts_1(spark, df_by_customer_id_1)

    return df_sum_amounts_1
