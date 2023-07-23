from abc import ABCMeta, abstractmethod

class DbConnector(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, **conf):
        raise NotImplementedError

    @abstractmethod
    def connect(self):
        raise NotImplementedError
