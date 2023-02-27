from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, ):
        self.spark = None
        self.update()

    def update(self, ):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        pass
