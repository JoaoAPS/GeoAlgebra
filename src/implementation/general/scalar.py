from interfaces.scalar import AbstractScalar


class GeneralScalar(AbstractScalar, float):

    def __str__(self):
        return str(float(self))

    def __repr__(self):
        return f'Scalar({float(self)})'
