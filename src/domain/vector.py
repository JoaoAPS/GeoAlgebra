from __future__ import annotations

import math
from numbers import Number
from typing import Optional, Union, Tuple

from .abstract import AbstractVector


class Vector(AbstractVector):

    def __init__(
        self,
        x_or_tuple: Optional[Union[float, tuple]] = None,
        y: float = 0.0
    ):
        if x_or_tuple is None:
            x_or_tuple = 0.0
        if isinstance(x_or_tuple, tuple):
            self._assign_components(x_or_tuple[0], x_or_tuple[1])
        else:
            self._assign_components(x_or_tuple, y)

    def _assign_components(self, x: float, y: float):
        error_msg = "Can't create Vector with component {} of type {}."
        if not isinstance(x, Number):
            raise TypeError(error_msg.format('x', type(x)))
        if not isinstance(y, Number):
            raise TypeError(error_msg.format('y', type(y)))
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def components(self) -> Tuple[float, float]:
        return (self._x, self._y)

    @property
    def modulus(self) -> float:
        return math.sqrt(sum(component**2 for component in self.components))

    @property
    def direction(self) -> Vector:
        pass
        # O Vector sabe fazer divisão?
        # return self / self.modulus

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.components == other.components

    def __str__(self) -> str:
        return f'{self.x}x + {self.y}y'

    def __repr__(self) -> str:
        return f'Vector2D({self.x}, {self.y})'
