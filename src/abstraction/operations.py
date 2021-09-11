from abc import ABC, abstractmethod

from abstraction.domain import Entity


class AbstractAdd(ABC):

    @abstractmethod
    def add(self, entity1: Entity, entity2: Entity) -> Entity:
        pass
