from implementation.general.element import GeneralElement
from implementation.space2d import Entity2D


class Element2D(Entity2D, GeneralElement):

    def __repr__(self):
        return f'Element2D({repr(self.scalar)}, {repr(self.vector)})'
    