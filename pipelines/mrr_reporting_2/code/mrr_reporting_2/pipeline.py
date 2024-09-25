from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting_2.config.ConfigStore import *
from mrr_reporting_2.functions import *
from prophecy.utils import *
from mrr_reporting_2.graph import *

def pipeline(spark: SparkSession) -> None:
    df_bronze_orders = bronze_orders(spark)
    df_bronze_customers = bronze_customers(spark)
    df_customer_order_details = customer_order_details(spark, df_bronze_customers, df_bronze_orders)
    df_total_spent_by_customer = total_spent_by_customer(spark, df_customer_order_details)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("mrr_reporting_2")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/mrr_reporting_2")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/mrr_reporting_2", config = Config)(pipeline)

if __name__ == "__main__":
    main()
