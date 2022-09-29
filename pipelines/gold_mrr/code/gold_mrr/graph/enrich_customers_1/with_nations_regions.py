from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gold_mrr.config.ConfigStore import *
from gold_mrr.udfs.UDFs import *

def with_nations_regions(
        spark: SparkSession,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame, 
        in3: DataFrame
) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.c_custkey") == col("in1.c_custkey")), "inner")\
        .join(in2.alias("in2"), (col("in2.n_nationkey") == col("in1.c_nationkey")), "inner")\
        .join(in3.alias("in3"), (col("in3.r_regionkey") == col("in2.n_regionkey")), "inner")\
        .select(col("in0.c_custkey").alias("c_custkey"), col("in3.r_name").alias("r_name"), col("in2.n_name").alias("n_name"), col("in0.amounts").alias("amounts"), col("in0.month").alias("month"))
