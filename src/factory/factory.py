from typing import Optional, Union, Tuple
from numbers import Number

from representation import ScalarData, VectorData  # , BivectorData, ElementData
from domain import Scalar, Vector  # , Bivector, Element
from abstraction.factory import AbstractFactory
from operations import Add


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
        if x is not None and y is not None:
            return self._make_vector_with_components(x, y)
        if components is not None:
            return self._make_vector_with_components(*components)

        if isinstance(x_or_components, tuple):
            return self._make_vector_with_components(*x_or_components)

        if x is not None:
            _x = x
        elif x_or_components is not None:
            _x = x_or_components
        else:
            _x = 0.0

        if y is not None:
            _y = y
        elif positional_y is not None:
            _y = positional_y
        else:
            _y = 0.0

        return self._make_vector_with_components(_x, _y)

    def _make_vector_with_components(self, x: float, y: float):
        error_msg = "Can't create Vector with component {} of type {}."
        if not isinstance(x, Number) or isinstance(x, bool):
            raise TypeError(error_msg.format('x', type(x).__name__))
        if not isinstance(y, Number) or isinstance(y, bool):
            raise TypeError(error_msg.format('y', type(y).__name__))
        vector_data = VectorData(x, y)
        return Vector(vector_data, self.adder)

    def make_bivector(self, *args, **kwargs):
        pass

    def make_element(self, *args, **kwargs):
        pass
