from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from cleanup_customers.config.ConfigStore import *
from cleanup_customers.udfs import *
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
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/cleanup_customers")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/cleanup_customers", config = Config)(pipeline)

if __name__ == "__main__":
    main()
