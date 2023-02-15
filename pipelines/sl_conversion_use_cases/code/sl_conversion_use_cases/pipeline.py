from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sl_conversion_use_cases.config.ConfigStore import *
from sl_conversion_use_cases.udfs.UDFs import *
from prophecy.utils import *
from sl_conversion_use_cases.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_customers_0 = silver_customers_0(spark)
    df_PipelineCall = PipelineCall(spark, df_silver_customers_0)
    CustomEmail_1(spark, df_PipelineCall)
    df_CustomEmail = CustomEmail(spark, df_silver_customers_0)
    UpsertSQL(spark, df_silver_customers_0)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/sl_conversion_use_cases")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/sl_conversion_use_cases")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
