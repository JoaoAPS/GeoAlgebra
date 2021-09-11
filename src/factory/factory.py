from typing import Optional, Union, Tuple
from numbers import Number

from representation import ScalarData  # , VectorData , BivectorData, ElementData
from domain import Scalar  # , Vector, Bivector, Element
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
        x_or_tuple: Optional[Union[float, Tuple[float, float]]] = None,
        y: Optional[float] = None,
        x: Optional[float] = None
    ):
        # TODO
        pass
        # if x is not None:
        #     pass

        # if x_or_tuple is None:
        #     x_or_tuple = 0.0
        # if isinstance(x_or_tuple, tuple):
        #     self._assign_components(x_or_tuple[0], x_or_tuple[1])
        # else:
        #     self._assign_components(x_or_tuple, y)

    def _assign_components(self, x: float, y: float):
        pass
        # error_msg = "Can't create Vector with component {} of type {}."
        # if not isinstance(x, Number) or isinstance(x, bool):
        #     raise TypeError(error_msg.format('x', type(x).__name__))
        # if not isinstance(y, Number) or isinstance(y, bool):
        #     raise TypeError(error_msg.format('y', type(y).__name__))
        # self._x = float(x)
        # self._y = float(y)

    def make_bivector(self, *args, **kwargs):
        pass

    def make_element(self, *args, **kwargs):
        pass
