from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from mrr_reporting.config.ConfigStore import *
from mrr_reporting.functions import *

@instrument
def data_quality_check(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
    import re
    from pydeequ.checks import Check, CheckLevel, ConstrainableDataTypes
    from pydeequ.verification import VerificationSuite, VerificationResult

    return (in0,
            VerificationResult\
              .checkResultsAsDataFrame(
                spark,
                VerificationSuite(spark)\
                  .onData(in0)\
                  .addCheck(
                    Check(spark, CheckLevel.Warning, "Data Quality Checks")\
                      .hasCompleteness("o_orderkey", lambda x: x >= 1.0, hint = f"{1.0 * 100}% values should be non-null for o_orderkey")
                  )\
                  .run()
              )\
              .selectExpr("constraint_status", "constraint_message", "udf_extract_check_and_column(constraint) as parsed")\
              .selectExpr("parsed._1 as check_type", "parsed._2 as column", "constraint_status", "constraint_message"))
