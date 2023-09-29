from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, user_name: str="enter_your_user_name", test: str="TRUE", **kwargs):
        self.user_name = user_name
        self.test = test
        pass

    def update(self, updated_config):
        self.user_name = updated_config.user_name
        self.test = updated_config.test
        pass

Config = SubgraphConfig()
