from __future__ import annotations

from typing import Tuple

from abstraction.domain import Entity
from abstraction.operations import AbstractAdd
from representation import BivectorData


class Bivector(Entity):

    def __init__(self, vector_data: BivectorData, adder: AbstractAdd):
        if not isinstance(vector_data, BivectorData):
            raise TypeError('Expected vector_data of type BivectorData. '
                            f'Received {type(vector_data).__name__} instead.')
        if not isinstance(adder, AbstractAdd):
            raise TypeError('Expected adder to be an subtype of AbstractAdd. '
                            f'Received {type(adder).__name__} instead.')

        self._data = vector_data
        self._adder = adder

    @property
    def xy(self) -> float:
        return self._data.xy

    @property
    def components(self) -> Tuple[float]:
        return (self._data.xy, )

    @property
    def modulus(self) -> float:
        return abs(self._data.xy)

    @property
    def direction(self) -> Bivector:
        pass
        # return self / self.modulus

    def __str__(self) -> str:
        return f'{self._data.xy}xy'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(xy={self._data.xy})'

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self._data == other._data
        return False

    def __neg__(self) -> Bivector:
        negative_data = BivectorData(-self._data.xy)
        return Bivector(negative_data, self._adder)

    def __add__(self, other: Entity) -> Entity:
        return self._adder.add(self, other)

    def __radd__(self, other: Entity) -> Entity:
        return self._adder.add(other, self)

    def __abs__(self) -> float:
        return self.modulus
