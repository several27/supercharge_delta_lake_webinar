from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingest_orders.config.ConfigStore import *
from ingest_orders.functions import *
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
                .appName("ingest_orders")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ingest_orders")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/ingest_orders", config = Config)(pipeline)

if __name__ == "__main__":
    main()
