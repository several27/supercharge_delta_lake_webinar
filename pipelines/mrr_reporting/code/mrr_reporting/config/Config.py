from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, user_name: str=None, test: str=None, **kwargs):
        self.spark = None
        self.update(user_name, test)

    def update(self, user_name: str="enter_your_user_name", test: str="TRUE", **kwargs):
        prophecy_spark = self.spark
        self.user_name = user_name
        self.test = test
        pass
