from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs import *

def create_temp_view(spark: SparkSession, in0: DataFrame) -> DataFrame:
    in0.createOrReplaceTempView("test_view")
    out0 = in0

    return out0
