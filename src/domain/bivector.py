from __future__ import annotations

from typing import Tuple

from abstraction.domain import Entity
from abstraction.operations import Operator
from representation import BivectorData


class Bivector(Entity):

    def __init__(self, vector_data: BivectorData, operator: Operator):
        if not isinstance(vector_data, BivectorData):
            raise TypeError('Expected vector_data of type BivectorData. '
                            f'Received {type(vector_data).__name__} instead.')
        if not isinstance(operator, Operator):
            raise TypeError('Expected operator to be of type Operator. '
                            f'Received {type(operator).__name__} instead.')

        self._data = vector_data
        self._operator = operator

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
        return Bivector(negative_data, self._operator)

    def __add__(self, other: Entity) -> Entity:
        return self._operator.add(self, other)

    def __radd__(self, other: Entity) -> Entity:
        return self._operator.add(other, self)

    def __abs__(self) -> float:
        return self.modulus
