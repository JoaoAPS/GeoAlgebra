from __future__ import annotations

import math
from typing import Tuple

from abstraction.domain import Entity
from abstraction.operations import AbstractAdd
from representation import VectorData


class Vector(Entity):

    def __init__(self, vector_data: VectorData, adder: AbstractAdd):
        if not isinstance(vector_data, VectorData):
            raise TypeError('Expected vector_data of type VectorData. '
                            f'Received {type(vector_data).__name__} instead.')
        if not isinstance(adder, AbstractAdd):
            raise TypeError('Expected adder to be an subtype of AbstractAdd. '
                            f'Received {type(adder).__name__} instead.')

        self._data = vector_data
        self._adder = adder

    @property
    def x(self) -> float:
        return self._data.x

    @property
    def y(self) -> float:
        return self._data.y

    @property
    def components(self) -> Tuple[float, float]:
        return (self._data.x, self._data.y)

    @property
    def modulus(self) -> float:
        return math.sqrt(sum(component**2 for component in self.components))

    @property
    def direction(self) -> Vector:
        pass
        # return self / self.modulus

    def __str__(self) -> str:
        return f'{self._data.x}x + {self._data.y}y'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(x={self._data.x}, y={self._data.y})'

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self._data == other._data
        if isinstance(other, tuple):
            return self.components == other
        return False

    def __neg__(self) -> Vector:
        negative_data = VectorData(-self._data.x, -self._data.y)
        return Vector(negative_data, self._adder)

    def __add__(self, other: Entity) -> Entity:
        return self._adder.add(self, other)

    def __radd__(self, other: Entity) -> Entity:
        return self._adder.add(other, self)

    def __abs__(self) -> float:
        return self.modulus
