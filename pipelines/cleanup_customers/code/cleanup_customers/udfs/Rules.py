from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *

@execute_rule
def test_rule(test: Column=lambda: col("test")):
    return when((test == lit(1)), (lit(True) == lit(True))).alias("new_rule")
