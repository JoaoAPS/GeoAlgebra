from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def make_scalar(self, *args, **kwargs):
        pass

    @abstractmethod
    def make_vector(self, *args, **kwargs):
        pass

    @abstractmethod
    def make_bivector(self, *args, **kwargs):
        pass

    @abstractmethod
    def make_element(self, *args, **kwargs):
        pass
