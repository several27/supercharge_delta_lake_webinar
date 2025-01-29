from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingest_customers.config.ConfigStore import *
from ingest_customers.udfs import *
from prophecy.utils import *
from ingest_customers.graph import *

def pipeline(spark: SparkSession) -> None:
    df_raw_customers = raw_customers(spark)
    bronze_customers_1(spark, df_raw_customers)

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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ingest_customers")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/ingest_customers", config = Config)(pipeline)

if __name__ == "__main__":
    main()
