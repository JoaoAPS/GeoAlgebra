from domain.scalar import Scalar
from domain.vector import Vector
from domain.bivector import Bivector
from domain.element import Element
from .abstract import AbstractFactory


class Factory(AbstractFactory):

    def scalar(self, *args, **kwargs):
        return Scalar(*args, **kwargs)

    def vector(self, *args, **kwargs):
        return Vector(*args, **kwargs)

    def bivector(self, *args, **kwargs):
        return Bivector(*args, **kwargs)

    def element(self, *args, **kwargs):
        return Element(*args, **kwargs)
