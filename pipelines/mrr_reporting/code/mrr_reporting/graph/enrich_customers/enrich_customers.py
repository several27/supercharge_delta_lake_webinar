from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def enrich_customers(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_customer_nations_1 = customer_nations_1(spark)
    df_customer_nations_1 = collectMetrics(
        spark, 
        df_customer_nations_1, 
        "enrich_customers", 
        "8eOw1j3e3CItKTNmDDtQC$$QidAPF8M-1JkxpPF2QZSZ", 
        "baY66HN4wc4uXEqdGmmMz$$ToN2MRvkITIYUNQ0uxNLk"
    )
    df_nation_1 = nation_1(spark)
    df_nation_1 = collectMetrics(
        spark, 
        df_nation_1, 
        "enrich_customers", 
        "Qi9M0IReFG82IosR2-wvm$$ZI3ClZC_jrgzpU5b49VIO", 
        "_2-MowCcC6LB7xy-ervYI$$7VzHnjb0r4aV2d04CfRHZ"
    )
    df_regions_1 = regions_1(spark)
    df_regions_1 = collectMetrics(
        spark, 
        df_regions_1, 
        "enrich_customers", 
        "wBzXOsVm1Ims8PFu5uirM$$jyxRbz5PBUB1gE-iyT7LG", 
        "IVsTJWG5L38m_YcVGnxAp$$lyR0Ci4IK1ZjfCX4VdOIV"
    )
    df_with_nations_regions_1 = with_nations_regions_1(spark, in0, df_customer_nations_1, df_nation_1, df_regions_1)
    df_with_nations_regions_1 = collectMetrics(
        spark, 
        df_with_nations_regions_1, 
        "enrich_customers", 
        "POGYtsQcVRaz-XBh40WU7$$015INLkZfpaQEArUSnoK9", 
        "5LNDDnlNXCSiiCfhTIIAT$$PqRk7BZ4kYt5PRJRGfjPK"
    )
    df_cleanup_1 = cleanup_1(spark, df_with_nations_regions_1)
    df_cleanup_1 = collectMetrics(
        spark, 
        df_cleanup_1, 
        "enrich_customers", 
        "CctApCXIwu-ZGepAFrzZ6$$VS7CDY_E-16hSS4Pdb35a", 
        "hutovkFDE9e5a1ulh67aD$$nNN_RfTjkTI2epB8XYXrp"
    )

    return df_cleanup_1
