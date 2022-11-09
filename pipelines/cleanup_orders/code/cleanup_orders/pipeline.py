from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from cleanup_orders.config.ConfigStore import *
from cleanup_orders.udfs.UDFs import *
from prophecy.utils import *
from cleanup_orders.graph import *

def pipeline(spark: SparkSession) -> None:
    df_bronze_orders = bronze_orders(spark)
    silver_orders(spark, df_bronze_orders)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/cleanup_orders")
    
    MetricsCollector.start(
        spark = spark,
        pipelineId = spark.conf.get("prophecy.project.id") + "/" + "pipelines/cleanup_orders"
    )
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
