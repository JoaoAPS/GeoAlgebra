from domain import EntityData, ScalarData, VectorData
from .abstract import AbstractAdd


class VectorAdd(AbstractAdd):

    def add(self, entity1: VectorData, entity2: EntityData):
        if isinstance(entity2, ScalarData):
            return self._add_scalar_with_vector(entity2, entity1)
        if isinstance(entity2, VectorData):
            return self._add_vectors(entity1, entity2)
        raise NotImplementedError()

    def _add_vectors(self, vector1: VectorData, vector2: VectorData):
        new_components = (
            v1_comp + v2_comp
            for v1_comp, v2_comp in zip(vector1.components, vector2.components)
        )
        return self.factory.vector(*new_components)

    def _add_scalar_with_vector(
        self, scalar: ScalarData, vector: VectorData
    ):
        return self.factory.element(scalar, vector)

