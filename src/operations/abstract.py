from abc import ABC, abstractmethod
from domain.abstract import Entity
from factory.abstract import AbstractFactory


class AbstractAdd(ABC):

    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    @abstractmethod
    def add(self, entity1: Entity, entity2: Entity):
        pass
