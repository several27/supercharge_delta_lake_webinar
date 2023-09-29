from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from mrr_reporting.udfs.UDFs import *

def Script_1(spark: SparkSession):
    print(Config.test)

    return 
