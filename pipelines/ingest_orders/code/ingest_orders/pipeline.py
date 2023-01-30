from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingest_orders.config.ConfigStore import *
from ingest_orders.udfs.UDFs import *
from prophecy.utils import *
from ingest_orders.graph import *

def pipeline(spark: SparkSession) -> None:
    df_raw_orders = raw_orders(spark)
    bronze_orders(spark, df_raw_orders)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ingest_orders")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/ingest_orders")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
