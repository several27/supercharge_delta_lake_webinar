from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from demo_day.config.ConfigStore import *
from demo_day.udfs.UDFs import *
from prophecy.utils import *
from demo_day.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_customers = silver_customers(spark)
    df_silver_orders = silver_orders(spark)
    df_by_customer_id = by_customer_id(spark, df_silver_orders, df_silver_customers)
    df_sum_amounts = sum_amounts(spark, df_by_customer_id)
    df_enrich_customers = enrich_customers(spark, Config.enrich_customers, df_sum_amounts)
    final_table(spark, df_enrich_customers)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/demo_day")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/demo_day", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/demo_day")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
