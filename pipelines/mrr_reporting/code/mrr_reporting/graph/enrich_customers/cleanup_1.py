from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from mrr_reporting.udfs import *

def cleanup_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("c_custkey"), 
        col("r_name").alias("region"), 
        col("n_name").alias("nation"), 
        concat(format_number(col("amounts"), 2), lit("z\u0142")).alias("amounts"), 
        when((col("month") == lit(1)), lit("January"))\
          .when((col("month") == lit(2)), lit("February"))\
          .when((col("month") == lit(3)), lit("March"))\
          .when((col("month") == lit(4)), lit("April"))\
          .when((col("month") == lit(5)), lit("May"))\
          .when((col("month") == lit(6)), lit("June"))\
          .when((col("month") == lit(7)), lit("July"))\
          .when((col("month") == lit(8)), lit("August"))\
          .when((col("month") == lit(9)), lit("September"))\
          .when((col("month") == lit(10)), lit("October"))\
          .when((col("month") == lit(11)), lit("November"))\
          .otherwise(lit("December"))\
          .alias("month")
    )
