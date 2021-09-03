from numbers import Number
from implementation.space2d import Entity2D
from implementation.general.vector import GeneralVector

class Vector2D(Entity2D, GeneralVector):

    def __init__(self, x: float, y: float = None):
        if type(x) is tuple:
            self._assign_components(x[0], x[1])
        else:
            self._assign_components(x, y)

    def _assign_components(self, x: float, y: float):
        error_msg = "Can't create vector with component of type {}."
        if not isinstance(x, Number):
            raise TypeError(error_msg.format(type(x)))
        if not isinstance(y, Number):
            raise TypeError(error_msg.format(type(y)))
        self.x = float(x)
        self.y = float(y)

    @property
    def components(self):
        return (self.x, self.y)

    def __str__(self):
        return f'{self.x}x + {self.y}y'

    def __repr__(self):
        return f'Vector2D({self.x}, {self.y})'
