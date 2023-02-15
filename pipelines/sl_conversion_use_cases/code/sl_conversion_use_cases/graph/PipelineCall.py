from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sl_conversion_use_cases.config.ConfigStore import *
from sl_conversion_use_cases.udfs.UDFs import *

def PipelineCall(spark: SparkSession, in0: DataFrame) -> DataFrame:
    import requests
    # STEP 1: Enter your workspace ID here
    domain = 'https://dbc-147abc45-b6c7.cloud.databricks.com'
    # STEP 2: Ensure you have a workspace.token secret created and accessible
    token = dbutils.secrets.get(scope = 'workspace', key = 'token')
    response = requests.post(
        '%s/api/2.1/jobs/run-now' % (domain),
        headers = {'Authorization' : 'Bearer %s' % token},
        # STEP 3: Enter a job_id you'd like to trigger
        json = {'job_id' : '549136548916411'}
    )

    if response.status_code == 200:
        print(response.json())
    else:
        raise Exception('An error occurred triggering the job. Complete error: %s' % (response.json()))

    out0 = spark.read.table("metadat")

    return out0
