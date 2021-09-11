from typing import Union
from numbers import Number

from abstraction.domain import Entity
from abstraction.operations import AbstractAdd
from representation import ScalarData
from utils.typing import is_number


class Scalar(Entity):

    def __init__(self, scalar_data: ScalarData, adder: AbstractAdd):
        if not isinstance(scalar_data, ScalarData):
            raise TypeError('Expected scalar_data of type ScalarData. '
                            f'Received {type(scalar_data).__name__} instead.')
        if not isinstance(adder, AbstractAdd):
            raise TypeError('Expected adder to be an subtype of AbstractAdd. '
                            f'Received {type(adder).__name__} instead.')

        self._data = scalar_data
        self._adder = adder

    @property
    def value(self) -> float:
        return self._data.value

    def __str__(self) -> str:
        return str(self._data.value)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._data.value})'

    def __float__(self) -> float:
        return float(self._data.value)

    def __eq__(self, other) -> bool:
        if isinstance(other, Scalar):
            return self._data == other._data
        if is_number(other):
            return self._data.value == other
        return False

    def __add__(self, other: Union[Entity, Number]) -> Entity:
        return self._adder.add(self, other)

    def __radd__(self, other: Union[Entity, Number]) -> Entity:
        return self._adder.add(other, self)

    def __abs__(self) -> float:
        return abs(float(self))
