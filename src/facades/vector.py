from interfaces import AbstractVector


class VectorFacade:

    def __init__(self, vector: AbstractVector):
        self.vector = vector

    def __str__(self):
        return str(self.vector)

    def __repr__(self):
        return repr(self.vector)

    @property
    def components(self):
        return self.vector.components

    @property
    def modulus(self):
        return self.vector.modulus

    @property
    def direction(self):
        return self.vector.direction
