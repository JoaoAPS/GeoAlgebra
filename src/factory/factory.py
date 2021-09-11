from typing import Optional, Union, Tuple
from numbers import Number

from representation import ScalarData, VectorData, BivectorData  # , ElementData
from domain import Scalar, Vector, Bivector  # , Element
from abstraction.factory import AbstractFactory
from operations import Add
from utils.typing import is_number


class Factory(AbstractFactory):

    def __init__(self):
        self.adder = Add(self)

    def make_scalar(
        self,
        value: Optional[Union[Scalar, ScalarData, Number]] = None
    ):
        if value is None:
            return Scalar(ScalarData(), self.adder)
        if isinstance(value, Scalar):
            return value
        if isinstance(value, ScalarData):
            return Scalar(value, self.adder)
        if isinstance(value, Number) and not isinstance(value, bool):
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
    ):
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

    def make_bivector(self, xy: Optional[float] = None):
        if xy is None:
            return Bivector(BivectorData(), self.adder)
        if isinstance(xy, Bivector):
            return xy
        if isinstance(xy, BivectorData):
            return Bivector(xy, self.adder)
        if isinstance(xy, Number) and not isinstance(xy, bool):
            bivector_data = BivectorData(float(xy))
            return Bivector(bivector_data, self.adder)
        raise TypeError(
            f"Cannot create bivector with xy of type {type(xy).__name__}.")

    def make_element(self, *args, **kwargs):
        pass
