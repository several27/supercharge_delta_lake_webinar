from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, user_name: str=None):
        self.spark = None
        self.update(user_name)

    def update(self, user_name: str="enter_your_user_name"):
        self.user_name = user_name
        pass
