from abc import ABC, abstractmethod


class Entity(ABC):
    pass


class AbstractScalar(Entity):

    @property
    @abstractmethod
    def value(self):
        pass


class AbstractVector(Entity):

    @property
    @abstractmethod
    def x(self):
        pass

    @property
    @abstractmethod
    def y(self):
        pass

    @property
    @abstractmethod
    def components(self):
        pass

    @property
    @abstractmethod
    def modulus(self):
        pass

    @property
    @abstractmethod
    def direction(self):
        pass


class AbstractBivector(Entity):

    @property
    @abstractmethod
    def xy(self):
        pass

    @property
    @abstractmethod
    def components(self):
        pass

    @property
    @abstractmethod
    def modulus(self):
        pass

    @property
    @abstractmethod
    def direction(self):
        pass


class AbstractElement(Entity):

    @property
    @abstractmethod
    def scalar(self):
        pass

    @property
    @abstractmethod
    def vector(self):
        pass

    @property
    @abstractmethod
    def bivector(self):
        pass

    @property
    @abstractmethod
    def x(self):
        pass

    @property
    @abstractmethod
    def y(self):
        pass

    @property
    @abstractmethod
    def xy(self):
        pass

    @property
    @abstractmethod
    def components(self):
        pass

    @property
    @abstractmethod
    def modulus(self):
        pass
