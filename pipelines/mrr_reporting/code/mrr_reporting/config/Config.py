from mrr_reporting.graph.enrich_customers.config.Config import SubgraphConfig as enrich_customers_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, user_name: str=None, enrich_customers: dict=None, **kwargs):
        self.spark = None
        self.update(user_name, enrich_customers)

    def update(self, user_name: str="enter_your_user_name", enrich_customers: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.user_name = user_name
        self.enrich_customers = self.get_config_object(
            prophecy_spark, 
            enrich_customers_Config(prophecy_spark = prophecy_spark), 
            enrich_customers, 
            enrich_customers_Config
        )
        pass
