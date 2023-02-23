from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, user_name: str=None):
        self.spark = None
        self.update(user_name)

    def update(self, user_name: str="enter_your_user_name"):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.user_name = user_name
        pass
