from implementation.space2d import Entity2D
from implementation.general.vector import GeneralVector

class Vector2D(Entity2D, GeneralVector):

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def components(self):
        return (self.x, self.y)

    def __str__(self):
        return f'{self.x}x + {self.y}y'

    def __repr__(self):
        return f'Vector2D({self.x}, {self.y})'
