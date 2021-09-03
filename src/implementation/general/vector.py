import math
from interfaces.vector import Vector

class GeneralVector(Vector):
    
    @property
    def modulus(self):
        return math.sqrt(sum(component**2 for component in self.components))

    @property
    def direction(self):
        return self / self.modulus
