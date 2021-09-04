from __future__ import annotations

from numbers import Number
from typing import Tuple, Optional

from .abstract import AbstractBivector


class Bivector(AbstractBivector):

    def __init__(self, xy: Optional[float] = None):
        if xy is None:
            xy = 0.0
        if not isinstance(xy, Number) or isinstance(xy, bool):
            raise TypeError("Can't create Bivector with component of type "
                            f"{type(xy).__name__}.")
        self._xy = float(xy)

    @property
    def xy(self) -> float:
        return self._xy

    @property
    def components(self) -> Tuple[float]:
        return (self._xy,)

    @property
    def modulus(self) -> float:
        return abs(self._xy)

    @property
    def direction(self) -> Bivector:
        # TODO
        pass

    def __eq__(self, other) -> bool:
        if type(other) is not self.__class__:
            return False
        return self.xy == other.xy

    def __str__(self) -> str:
        return f'{self.xy}xy'

    def __repr__(self) -> str:
        return f'Bivector({self.xy})'
