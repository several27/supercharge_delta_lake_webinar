from mrr_reporting.graph.enrich_customers_1.config.Config import SubgraphConfig as enrich_customers_1_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, user_name: str=None, enrich_customers_1: dict=None, **kwargs):
        self.spark = None
        self.update(user_name, enrich_customers_1)

    def update(self, user_name: str="enter_your_user_name", enrich_customers_1: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.user_name = user_name
        self.enrich_customers_1 = self.get_config_object(
            prophecy_spark, 
            enrich_customers_1_Config(prophecy_spark = prophecy_spark), 
            enrich_customers_1, 
            enrich_customers_1_Config
        )
        pass
