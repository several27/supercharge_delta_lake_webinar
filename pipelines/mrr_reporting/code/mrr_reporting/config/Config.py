from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, filterExpression: str=None):
        self.spark = None
        self.update(filterExpression)

    def update(self, filterExpression: str="in0.c_custkey = 1"):
        self.filterExpression = filterExpression
        pass
