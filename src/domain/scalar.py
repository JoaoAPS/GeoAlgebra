from numbers import Number
from typing import Optional

from .abstract import AbstractScalar

class Scalar(AbstractScalar):

    def __init__(self, value: Optional[float] = None):
        if value is None:
            value = 0.0
        if not isinstance(value, Number) or isinstance(value, bool):
            raise TypeError("Can't create Scalar with component value of type "
                            f"{type(value).__name__}.")
        self._value = float(value)

    @property
    def value(self) -> float:
        return self._value

    def __float__(self) -> float:
        return self._value

    def __eq__(self, other) -> bool:
        if not isinstance(other, Scalar) and not isinstance(other, Number):
            return False
        return float(self) == float(other)

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f'Scalar({self._value})'
