from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *
from prophecy.utils import *
from mrr_reporting.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_orders_0 = silver_orders_0(spark)
    df_silver_customers_2 = silver_customers_2(spark)
    df_by_customer_id = by_customer_id(spark, df_silver_orders_0, df_silver_customers_2)
    df_Limit_1 = Limit_1(spark, df_by_customer_id)
    df_sum_spendings = sum_spendings(spark, df_Limit_1)
    df_enrich_customers_1 = enrich_customers_1(spark, df_sum_spendings)
    gold_report(spark, df_enrich_customers_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "3436/pipelines/mrr_reporting")
    MetricsCollector.start(spark = spark, pipelineId = "3436/pipelines/mrr_reporting")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
