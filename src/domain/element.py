from __future__ import annotations

from typing import Tuple

from abstraction.domain import Entity
from abstraction.operations import Operator
from domain import Scalar, Vector, Bivector


class Element(Entity):

    def __init__(
        self,
        scalar: Scalar,
        vector: Vector,
        bivector: Bivector,
        operator: Operator,
    ):
        if not isinstance(scalar, Scalar):
            raise TypeError('Expected scalar of type Scalar. '
                            f'Received {type(scalar).__name__} instead.')
        if not isinstance(vector, Vector):
            raise TypeError('Expected vector of type Vector. '
                            f'Received {type(vector).__name__} instead.')
        if not isinstance(bivector, Bivector):
            raise TypeError('Expected bivector of type Bivector. '
                            f'Received {type(bivector).__name__} instead.')
        if not isinstance(operator, Operator):
            raise TypeError('Expected operator to be of type Operator. '
                            f'Received {type(operator).__name__} instead.')

        self._scalar = scalar
        self._vector = vector
        self._bivector = bivector
        self._operator = operator

    @property
    def scalar(self) -> float:
        return self._scalar

    @property
    def vector(self) -> float:
        return self._vector

    @property
    def bivector(self) -> float:
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
        return (
            self._scalar.value,
            self._vector.x,
            self._vector.y,
            self._bivector.xy
        )

    @property
    def modulus(self) -> float:
        pass

    def __str__(self) -> str:
        return (f'{self._scalar.value} + {self._vector.x}x + '
                f'{self._vector.y}y + {self._bivector.xy}xy')

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}({repr(self._scalar)}, '
                f'{repr(self._vector)}, {repr(self._bivector)})')

    def __add__(self, other: Entity) -> Entity:
        return self._operator.add(self, other)

    def __radd__(self, other: Entity) -> Entity:
        return self._operator.add(other, self)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Entity):
            return False
        if isinstance(other, self.__class__):
            return self._is_element_equal(other)
        if isinstance(other, Scalar):
            return self._is_scalar_equal(other)
        if isinstance(other, Vector):
            return self._is_vector_equal(other)
        if isinstance(other, Bivector):
            return self._is_bivector_equal(other)
        return False

    def __neg__(self) -> Element:
        return Element(
            -self._scalar, -self.vector, -self.bivector, self._operator)

    def _is_element_equal(self, other: Element) -> bool:
        for component in ['_scalar', '_vector', '_bivector']:
            if getattr(self, component) != getattr(other, component):
                return False
        return True

    def _is_scalar_equal(self, other: Scalar) -> bool:
        if self._vector.components != (0.0, 0.0):
            return False
        if self._bivector.xy != 0.0:
            return False
        return self._scalar == other

    def _is_vector_equal(self, other: Vector) -> bool:
        if self._scalar.value != 0.0:
            return False
        if self._bivector.xy != 0.0:
            return False
        return self._vector == other

    def _is_bivector_equal(self, other: Bivector) -> bool:
        if self._scalar.value != 0.0:
            return False
        if self._vector.components != (0.0, 0.0):
            return False
        return self._bivector == other
