from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *

def data_cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df_sum_amounts_1 = sum_amounts_1(spark, in0)
    df_floor_amounts_1 = floor_amounts_1(spark, df_sum_amounts_1)
    df_cleanup_amounts_1 = cleanup_amounts_1(spark, df_floor_amounts_1)

    return df_cleanup_amounts_1
