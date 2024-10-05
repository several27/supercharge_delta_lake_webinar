from mrr_reporting.graph.enrich_customers.config.Config import SubgraphConfig as enrich_customers_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, enrich_customers: dict=None, **kwargs):
        self.spark = None
        self.update(enrich_customers)

    def update(self, enrich_customers: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.enrich_customers = self.get_config_object(
            prophecy_spark, 
            enrich_customers_Config(prophecy_spark = prophecy_spark), 
            enrich_customers, 
            enrich_customers_Config
        )
        pass
