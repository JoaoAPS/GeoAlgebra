from interfaces.scalar import Scalar

class GeneralScalar(Scalar, int):

    def __repr__(self):
        return f'Scalar({int(self)})'
