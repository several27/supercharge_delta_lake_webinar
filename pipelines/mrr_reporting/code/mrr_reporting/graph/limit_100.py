from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *

def limit_100(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.limit(100)

    return df1.limit(100)
