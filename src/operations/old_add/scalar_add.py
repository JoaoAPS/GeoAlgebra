from domain import ScalarData
from .abstract import AbstractAdd


class ScalarAdd(AbstractAdd):

    def add(self, entity1: ScalarData, entity2: ScalarData):
        if not isinstance(entity2, ScalarData):
            raise NotImplementedError()
        return ScalarData(entity1.value + entity2.value)
