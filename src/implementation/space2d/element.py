from interfaces.element import AbstractElement
from implementation.space2d import Entity2D, Scalar2D, Vector2D


class Element2D(Entity2D, AbstractElement):

    def __init__(self, scalar: Scalar2D, vector: Vector2D):
        self.scalar = scalar
        self.vector = vector

    def __str__(self):
        return f'{self.scalar} + {self.vector}'

    def __repr__(self):
        return f'Element2D({repr(self.scalar)}, {repr(self.vector)})'
    