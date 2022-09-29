from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from cleanup_customers.config.ConfigStore import *
from cleanup_customers.udfs.UDFs import *
from prophecy.utils import *
from cleanup_customers.graph import *

def pipeline(spark: SparkSession) -> None:
    df_bronze_customers_0 = bronze_customers_0(spark)
    silver_customers(spark, df_bronze_customers_0)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "3436/pipelines/cleanup_customers")
    MetricsCollector.start(spark = spark, pipelineId = "3436/pipelines/cleanup_customers")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
