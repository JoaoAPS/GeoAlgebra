from interfaces import Entity, AbstractElement, AbstractScalar, AbstractVector


class GeneralElement(AbstractElement):

    def __init__(self, scalar: AbstractScalar, vector: AbstractVector):
        self.scalar = scalar
        self.vector = vector

    def __str__(self):
        return f'{self.scalar} + {self.vector}'

    def __eq__(self, other: AbstractElement):
        if type(other) is not self.__class__:
            raise TypeError(f'Cannot compare {self.__class__.__name__} with '
                            f'{type(other).__name__}.')
        return self.scalar == other.scalar and self.vector == other.vector
    