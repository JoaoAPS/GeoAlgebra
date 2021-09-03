from implementation.general.vector import GeneralVector

class Vector2D(GeneralVector):

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def components(self):
        return (self.x, self.y)

    def __repr__(self):
        return f'Vector2D({self.x}, {self.y})'
