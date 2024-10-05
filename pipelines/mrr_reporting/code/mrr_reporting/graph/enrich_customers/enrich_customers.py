from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from mrr_reporting.functions import *
from . import *
from .config import *

@instrument
def enrich_customers(spark: SparkSession, subgraph_config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(subgraph_config)
    df_customer_nations_1 = customer_nations_1(spark)
    df_nation_1 = nation_1(spark)
    df_regions_1 = regions_1(spark)
    df_with_nations_regions_1 = with_nations_regions_1(spark, in0, df_customer_nations_1, df_nation_1, df_regions_1)
    df_cleanup_1 = cleanup_1(spark, df_with_nations_regions_1)
    subgraph_config.update(Config)

    return df_cleanup_1
