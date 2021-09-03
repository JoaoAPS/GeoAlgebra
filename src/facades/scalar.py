from interfaces.scalar import AbstractScalar


class ScalarFacade:

    def __init__(self, scalar: AbstractScalar):
        self.scalar = scalar

    def __str__(self):
        return str(self.scalar)

    def __repr__(self):
        return repr(self.scalar)
