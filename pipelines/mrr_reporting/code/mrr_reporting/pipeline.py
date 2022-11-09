from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *
from prophecy.utils import *
from mrr_reporting.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silvers_orders = silvers_orders(spark)
    df_silver_customers_0 = silver_customers_0(spark)
    df_by_customer_id = by_customer_id(spark, df_silver_customers_0, df_silvers_orders)
    df_sum_amounts = sum_amounts(spark, df_by_customer_id)
    df_Reformat_1 = Reformat_1(spark, df_sum_amounts)
    df_enrich_customers_1 = enrich_customers_1(spark, df_Reformat_1)
    final_report(spark, df_enrich_customers_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/mrr_reporting")
    
    MetricsCollector.start(
        spark = spark,
        pipelineId = spark.conf.get("prophecy.project.id") + "/" + "pipelines/mrr_reporting"
    )
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
