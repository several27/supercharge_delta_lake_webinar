from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from mrr_reporting.graph.enrich_customers.cleanup_1 import *
from mrr_reporting.config.ConfigStore import *


class cleanup_1Test(BaseTestCase):

    def test_unit_test_1(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/mrr_reporting/graph/enrich_customers/cleanup_1/in0/schema.json',
            'test/resources/data/mrr_reporting/graph/enrich_customers/cleanup_1/in0/data/test_unit_test_1.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/mrr_reporting/graph/enrich_customers/cleanup_1/out/schema.json',
            'test/resources/data/mrr_reporting/graph/enrich_customers/cleanup_1/out/data/test_unit_test_1.json',
            'out'
        )
        dfOutComputed = cleanup_1(self.spark, dfIn0)
        assertDFEquals(dfOut.select("month"), dfOutComputed.select("month"), self.maxUnequalRowsToShow)

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        Utils.initializeFromArgs(
            self.spark,
            Namespace(
              file = f"configs/resources/config/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            ),
            "configs/resources/config/mrr_reporting.conf"
        )
