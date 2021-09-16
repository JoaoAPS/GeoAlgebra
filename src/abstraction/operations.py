from abc import ABC, abstractmethod

from abstraction.domain import Entity


class AbstractAdder(ABC):

    @abstractmethod
    def add(self, entity1: Entity, entity2: Entity) -> Entity:
        pass


class AbstractSubtractor:

    @abstractmethod
    def subtract(self, entity1: Entity, entity2: Entity) -> Entity:
        pass


class AbstractInnerProduct:

    @abstractmethod
    def inner(self, entity1: Entity, entity2: Entity) -> Entity:
        pass


class AbstractOuterProduct:

    @abstractmethod
    def outer(self, entity1: Entity, entity2: Entity) -> Entity:
        pass


class Operator:

    def __init__(
        self,
        adder: AbstractAdder,
        subtractor: AbstractSubtractor,
        inner_product: AbstractInnerProduct,
        outer_product: AbstractOuterProduct,
    ):
        self._adder = adder
        self._subtractor = subtractor
        self._inner_product = inner_product
        self._outer_product = outer_product

    def add(self, entity1: Entity, entity2: Entity) -> Entity:
        return self._adder.add(entity1, entity2)

    def subtract(self, entity1: Entity, entity2: Entity) -> Entity:
        return self._subtractor.subtract(entity1, entity2)

    def inner_product(self, entity1: Entity, entity2: Entity) -> Entity:
        return self._inner_product.inner_product(entity1, entity2)

    def outer_product(self, entity1: Entity, entity2: Entity) -> Entity:
        return self._outer_product.outer_product(entity1, entity2)
