from interfaces.scalar import Scalar

class GeneralScalar(Scalar, float):

    def __str__(self):
        return str(float(self))

    def __repr__(self):
        return f'Scalar({float(self)})'
