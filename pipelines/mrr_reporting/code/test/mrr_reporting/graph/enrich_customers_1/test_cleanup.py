from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from mrr_reporting.graph.enrich_customers_1.cleanup import *
import mrr_reporting.config.ConfigStore as ConfigStore


class cleanupTest(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/mrr_reporting/graph/enrich_customers_1/cleanup/in0/schema.json',
            'test/resources/data/mrr_reporting/graph/enrich_customers_1/cleanup/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/mrr_reporting/graph/enrich_customers_1/cleanup/out/schema.json',
            'test/resources/data/mrr_reporting/graph/enrich_customers_1/cleanup/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = cleanup(self.spark, dfIn0)
        assertDFEquals(dfOut.select("amounts"), dfOutComputed.select("amounts"), self.maxUnequalRowsToShow)

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        ConfigStore.Utils.initializeFromArgs(
            self.spark,
            Namespace(file = f"configs/resources/config/{fabricName}.json", config = None)
        )
