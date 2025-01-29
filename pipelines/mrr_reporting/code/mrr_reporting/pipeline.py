from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs import *
from prophecy.utils import *
from mrr_reporting.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_customers_2_1 = silver_customers_2_1(spark)
    df_silvers_orders = silvers_orders(spark)
    df_by_customer_id = by_customer_id(spark, df_silver_customers_2_1, df_silvers_orders)
    df_extract_order_month = extract_order_month(spark, df_by_customer_id)
    df_sum_amounts = sum_amounts(spark, df_extract_order_month)
    df_enrich_customers = enrich_customers(spark, Config.enrich_customers, df_sum_amounts)
    final_report(spark, df_enrich_customers)
    df_create_temp_view = create_temp_view(spark, df_silver_customers_2_1)
    df_create_customer_dataframe = create_customer_dataframe(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/mrr_reporting")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/mrr_reporting", config = Config)(pipeline)

if __name__ == "__main__":
    main()
