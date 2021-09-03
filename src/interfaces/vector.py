from interfaces.entity import Entity

class AbstractVector(Entity):

    @property
    def modulus(self):
        pass

    @property
    def components(self):
        pass
    
    @property
    def direction(self):
        pass
