from typing import Optional, Union, Tuple
from numbers import Number

from representation import ScalarData, VectorData, BivectorData
from domain import Scalar, Vector, Bivector, Element
from abstraction.factory import AbstractFactory
from operations import Add
from utils.typing import is_number


class Factory(AbstractFactory):

    def __init__(self):
        self.adder = Add(self)

    def make_scalar(
        self,
        value: Optional[Union[Scalar, ScalarData, Number]] = None
    ) -> Scalar:
        if value is None:
            return Scalar(ScalarData(), self.adder)
        if isinstance(value, Scalar):
            return value
        if isinstance(value, ScalarData):
            return Scalar(value, self.adder)
        if is_number(value):
            scalar_data = ScalarData(float(value))
            return Scalar(scalar_data, self.adder)
        raise TypeError(
            f"Cannot create scalar with value of type {type(value).__name__}.")

    def make_vector(
        self,
        x_or_components: Optional[Union[float, Tuple[float, float]]] = None,
        positional_y: Optional[float] = None,
        x: Optional[float] = None,
        y: Optional[float] = None,
        components: Optional[Tuple[float, float]] = None
    ) -> Vector:
        if isinstance(x_or_components, Vector):
            return x_or_components
        if isinstance(x_or_components, VectorData):
            return Vector(x_or_components, self.adder)

        if x is not None and y is not None:
            return self._make_vector_with_components(x, y)
        if components is not None:
            return self._make_vector_with_components(*components)

        if isinstance(x_or_components, tuple):
            return self._make_vector_with_components(*x_or_components)

        _x = self._find_first_non_none(x, x_or_components)
        _y = self._find_first_non_none(y, positional_y)
        return self._make_vector_with_components(_x, _y)

    def _make_vector_with_components(self, x: float, y: float):
        error_msg = "Can't create Vector with component {} of type {}."

        vector_data_kwargs = {}
        if x is not None:
            if not is_number(x):
                raise TypeError(error_msg.format('x', type(x).__name__))
            vector_data_kwargs['x'] = x
        if y is not None:
            if not is_number(y):
                raise TypeError(error_msg.format('y', type(y).__name__))
            vector_data_kwargs['y'] = y

        vector_data = VectorData(**vector_data_kwargs)
        return Vector(vector_data, self.adder)

    def _find_first_non_none(self, *args):
        for arg in args:
            if arg is not None:
                return arg
        return None

    def make_bivector(
        self,
        xy: Optional[Union[Number, Bivector, BivectorData]] = None
    ) -> Bivector:
        if xy is None:
            return Bivector(BivectorData(), self.adder)
        if isinstance(xy, Bivector):
            return xy
        if isinstance(xy, BivectorData):
            return Bivector(xy, self.adder)
        if is_number(xy):
            bivector_data = BivectorData(float(xy))
            return Bivector(bivector_data, self.adder)
        raise TypeError(
            f"Cannot create bivector with xy of type {type(xy).__name__}.")

    def make_element(
        self,
        wildcard1: Optional[Union[Number, Scalar, Tuple, Element]] = None,
        wildcard2: Optional[Union[Number, Vector]] = None,
        wildcard3: Optional[Union[Number, Bivector]] = None,
        wildcard4: Optional[Number] = None,
        scalar: Optional[Union[Number, Scalar]] = None,
        vector: Optional[Vector] = None,
        bivector: Optional[Bivector] = None,
        x: Optional[Number] = None,
        y: Optional[Number] = None,
        xy: Optional[Number] = None,
        components: Optional[Tuple[Number, Number, Number, Number]] = None,
    ) -> Element:
        if isinstance(wildcard1, Element):
            return wildcard1

        if isinstance(components, tuple) and len(components) < 4:
            raise ValueError(
                'Argument "components" must contain all 4 element components')
        if isinstance(wildcard1, tuple) and len(wildcard1) < 4:
            raise ValueError('First positional argument must contain all 4 '
                             'element components if passed as a tuple.')

        _scalar = self._get_scalar_from_arguments(
            scalar, wildcard1, components)
        _vector = self._get_vector_from_arguments(
            vector, x, y, wildcard1, wildcard2, wildcard3, components)
        _bivector = self._get_bivector_from_arguments(
            bivector,
            xy,
            components,
            wildcard1,
            wildcard2,
            wildcard3,
            wildcard4
        )
        return self._make_element_with_entities(_scalar, _vector, _bivector)

    def _get_scalar_from_arguments(self, scalar, wildcard1, components):
        if scalar is not None:
            return scalar
        if components is not None:
            return components[0]
        if isinstance(wildcard1, tuple):
            return wildcard1[0]
        if wildcard1 is not None:
            return wildcard1
        return self.make_scalar()

    def _get_vector_from_arguments(
        self, vector, x, y, wildcard1, wildcard2, wildcard3, components
    ):
        if vector is not None:
            return vector
        if x is not None or y is not None:
            return self.make_vector(x=x, y=y)
        if components is not None:
            return self.make_vector(x=components[1], y=components[2])
        if isinstance(wildcard1, tuple):
            return self.make_vector(x=wildcard1[1], y=wildcard1[2])
        if isinstance(wildcard2, Vector):
            return wildcard2
        if wildcard2 is not None:
            if wildcard3 is not None:
                return self.make_vector(wildcard2, wildcard3)
            else:
                return self.make_vector(wildcard2)
        return self.make_vector()

    def _get_bivector_from_arguments(
        self,
        bivector,
        xy,
        components,
        wildcard1,
        wildcard2,
        wildcard3,
        wildcard4
    ):
        if bivector is not None:
            return bivector
        if xy is not None:
            return self.make_bivector(xy)
        if components is not None:
            return self.make_bivector(components[3])
        if isinstance(wildcard1, tuple):
            return self.make_bivector(wildcard1[3])
        if isinstance(wildcard2, Vector):
            return self.make_bivector(wildcard3)
        if wildcard4 is not None:
            return self.make_bivector(wildcard4)
        return self.make_bivector()

    def _make_element_with_entities(
        self, scalar: Scalar, vector: Vector, bivector: Bivector
    ):
        if is_number(scalar):
            scalar = self.make_scalar(scalar)

        error_msg = "Can't create Element with {} component of type {}."
        if not isinstance(scalar, Scalar):
            raise TypeError(error_msg.format('scalar', type(scalar).__name__))
        if not isinstance(vector, Vector):
            raise TypeError(error_msg.format('vector', type(vector).__name__))
        if not isinstance(bivector, Bivector):
            raise TypeError(
                error_msg.format('bivector', type(bivector).__name__))

        return Element(
            scalar=scalar, vector=vector, bivector=bivector, adder=self.adder)
