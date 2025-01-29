from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.functions import *
from prophecy.utils import *
from mrr_reporting.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_orders = silver_orders(spark)
    df_silver_customers = silver_customers(spark)
    df_by_c_custkey_c_comment = by_c_custkey_c_comment(spark, df_silver_customers, df_silver_orders)
    df_reformat_order_customer_data = reformat_order_customer_data(spark, df_by_c_custkey_c_comment)
    df_total_amount_by_month_and_customer = total_amount_by_month_and_customer(spark, df_reformat_order_customer_data)
    df_enrich_customers = enrich_customers(spark, Config.enrich_customers, df_total_amount_by_month_and_customer)
    final_report_j(spark, df_enrich_customers)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("mrr_reporting")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/mrr_reporting")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/mrr_reporting", config = Config)(pipeline)

if __name__ == "__main__":
    main()
