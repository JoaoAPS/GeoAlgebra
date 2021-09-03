from __future__ import annotations
import math
from interfaces.vector import AbstractVector

class GeneralVector(AbstractVector):
    
    @property
    def modulus(self):
        return math.sqrt(sum(component**2 for component in self.components))

    @property
    def direction(self):
        return self / self.modulus

    def __eq__(self, other: AbstractVector):
        if type(other) is not self.__class__:
            raise TypeError(f'Cannot compare {self.__class__.__name__} with '
                            f'{type(other).__name__}.')
        return self.components == other.components
