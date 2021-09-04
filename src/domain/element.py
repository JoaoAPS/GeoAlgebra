from typing import Union, Optional, Tuple
from numbers import Number

from .abstract import AbstractElement
from .scalar import Scalar
from .vector import Vector
from .bivector import Bivector


class Element(AbstractElement):

    def __init__(
        self,
        scalar: Optional[Union[Scalar, float]] = None,
        x_or_vector: Optional[Union[Vector, float]] = None,
        y_or_bivector: Optional[Union[Bivector, float]] = None,
        xy: float = 0.0
    ):
        scalar, x_or_vector, y_or_bivector = self._default_initial_values(
            scalar, x_or_vector, y_or_bivector)

        self._scalar = Scalar(scalar)

        if not isinstance(x_or_vector, Vector):
            self._assign_vector_and_bivector_components(
                x_or_vector, y_or_bivector, xy)
        else:
            self._vector = x_or_vector
            self._bivector = (y_or_bivector
                              if isinstance(y_or_bivector, Bivector)
                              else Bivector(xy))

    def _default_initial_values(self, scalar, vector, bivector):
        if scalar is None:
            scalar = Scalar(0.0)
        if vector is None:
            vector = Vector()
        if bivector is None:
            bivector = Bivector()
        return scalar, vector, bivector

    def _assign_vector_and_bivector_components(
        self, x: float, y: float, xy: float
    ):
        error_msg = "Can't create Element with component {} of type {}."
        if not isinstance(x, Number):
            raise TypeError(error_msg.format('x', type(x).__name__))
        if not isinstance(y, Number):
            raise TypeError(error_msg.format('y', type(y).__name__))
        if not isinstance(xy, Number):
            raise TypeError(error_msg.format('xy', type(xy).__name__))
        self._vector = Vector(x, y)
        self._bivector = Bivector(xy)

    @property
    def scalar(self) -> Scalar:
        return self._scalar

    @property
    def vector(self) -> Vector:
        return self._vector

    @property
    def bivector(self) -> Bivector:
        return self._bivector

    @property
    def x(self) -> float:
        return self._vector.x

    @property
    def y(self) -> float:
        return self._vector.y

    @property
    def xy(self) -> float:
        return self._bivector.xy

    @property
    def components(self) -> Tuple[float, float, float, float]:
        return (float(self.scalar), self.x, self.y, self.xy)

    @property
    def modulus(self) -> float:
        # TODO
        pass

    def __eq__(self, other) -> bool:
        if type(other) is not self.__class__:
            return False
        return (
            self.scalar == other.scalar and
            self.vector == other.vector and
            self.bivector == other.bivector
        )

    def __str__(self) -> str:
        return f'{self.scalar} + {self.vector} + {self.bivector}'

    def __repr__(self) -> str:
        return (
            'Element(' +
            repr(self.scalar) + ', ' +
            repr(self.vector) + ', ' +
            repr(self.bivector) + ')'
        )
