from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *

def enrich_customers_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df_regions = regions(spark)
    df_customer_nations = customer_nations(spark)
    df_nation = nation(spark)
    df_with_nations_regions = with_nations_regions(spark, in0, df_customer_nations, df_nation, df_regions)
    df_cleanup = cleanup(spark, df_with_nations_regions)

    return df_cleanup
