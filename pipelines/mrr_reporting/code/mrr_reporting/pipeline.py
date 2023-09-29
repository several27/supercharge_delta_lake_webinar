from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.udfs.UDFs import *
from prophecy.utils import *
from mrr_reporting.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silvers_orders = silvers_orders(spark)
    df_silvers_orders = collectMetrics(
        spark, 
        df_silvers_orders, 
        "graph", 
        "pO5YHh3nZnXt-eVREgBwa$$wwag5Zt9iWd0hs9tAbgd7", 
        "OyKr4T8s7EaPCbahzQCaf$$txJeJUgRyd8-KmtA5nW_3"
    )
    df_silver_customers_2_1 = silver_customers_2_1(spark)
    df_silver_customers_2_1 = collectMetrics(
        spark, 
        df_silver_customers_2_1, 
        "graph", 
        "MypoFqL88fNcV5-mfyFvL$$STT-zlwIUB5G5yYtXluEy", 
        "iG3b_lBYNrvozN1jayuau$$OImvC0aVAhhf3irvxPGZu"
    )
    df_by_customer_id = by_customer_id(spark, df_silver_customers_2_1, df_silvers_orders)
    df_by_customer_id = collectMetrics(
        spark, 
        df_by_customer_id, 
        "graph", 
        "OZ1fXfONc7dlwERNlEvlV$$6eEd0VyCCEOJQgvFe2Anc", 
        "SVDH8nbIU0lEXyN3Fff9w$$V4vo6JH4H9bou1_ig4XgO"
    )
    df_sum_amounts = sum_amounts(spark, df_by_customer_id)
    df_sum_amounts = collectMetrics(
        spark, 
        df_sum_amounts, 
        "graph", 
        "-VL0ws3hNDRC027Xt5Pi5$$K_PD3mlYT6eYM2givfYyB", 
        "uhL8QtHGZrzOYy73BMscN$$TMVKLa4xkkt-T1icsFFas"
    )
    df_round_amounts = round_amounts(spark, df_sum_amounts)
    df_round_amounts = collectMetrics(
        spark, 
        df_round_amounts, 
        "graph", 
        "BzJA7ALfiS_uKJ_vtgjxv$$hTGXK8AUin5gduocpsR4q", 
        "EqkGx5buvxyHZTruinIiX$$Etp2OD2ZaFUcxxyyvF4To"
    )
    df_enrich_customers = enrich_customers(spark, Config.enrich_customers, df_round_amounts)
    final_report(spark, df_enrich_customers)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("spark.sql.optimizer.excludedRules", "org.apache.spark.sql.catalyst.optimizer.ColumnPruning")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/mrr_reporting")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/mrr_reporting", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/mrr_reporting")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
