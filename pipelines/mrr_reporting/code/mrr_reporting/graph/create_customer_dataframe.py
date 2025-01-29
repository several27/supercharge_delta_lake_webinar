from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs import *

def create_customer_dataframe(spark: SparkSession) -> DataFrame:
    # from pyspark.sql import Row
    # # Sample customer data
    # customer_data = [
    #     Row(customer_id=1, name="John Doe", age=30, email="john.doe@example.com"),
    #     Row(customer_id=2, name="Jane Smith", age=25, email="jane.smith@example.com"),
    #     Row(customer_id=3, name="Sam Brown", age=40, email="sam.brown@example.com")
    # ]
    # # Create DataFrame from sample data
    # out0 = spark.createDataFrame(customer_data)
    out0 = spark.sql("select * from test_view")

    return out0
