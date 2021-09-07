from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def scalar(self, *args, **kwargs):
        pass

    @abstractmethod
    def vector(self, *args, **kwargs):
        pass

    @abstractmethod
    def bivector(self, *args, **kwargs):
        pass

    @abstractmethod
    def element(self, *args, **kwargs):
        pass
