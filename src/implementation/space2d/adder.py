from interfaces.adder import AbstractAdder
from implementation.space2d import Entity2D, Scalar2D, Vector2D, Element2D


class Adder2D(AbstractAdder):

    def add(self, entity1: Entity2D, entity2: Entity2D):
        if isinstance(entity1, Scalar2D):
            if isinstance(entity2, Scalar2D):
                return self._add_scalars(entity1, entity2)
            if isinstance(entity2, Vector2D):
                return self._add_scalar_with_vector(entity1, entity2)
            if isinstance(entity2, Element2D):
                return self._add_element_with_scalar(entity2, entity1)

        if isinstance(entity1, Vector2D):
            if isinstance(entity2, Scalar2D):
                return self._add_scalar_with_vector(entity2, entity1)
            if isinstance(entity2, Vector2D):
                return self._add_vectors(entity1, entity2)
            if isinstance(entity2, Element2D):
                return self._add_element_with_vector(entity2, entity1)

        if isinstance(entity1, Element2D):
            if isinstance(entity2, Scalar2D):
                return self._add_element_with_scalar(entity1, entity2)
            if isinstance(entity2, Vector2D):
                return self._add_element_with_vector(entity1, entity2)
            if isinstance(entity2, Element2D):
                return self._add_elements(entity1, entity2)

        raise TypeError(f'Cannot add {type(entity1)} with {type(entity2)}')

    def _add_scalars(self, scalar1: Scalar2D, scalar2: Scalar2D):
        return Scalar2D(scalar1 + scalar2)

    def _add_vectors(self, vector1: Vector2D, vector2: Vector2D):
        new_components = (
            v1_comp + v2_comp
            for v1_comp, v2_comp in zip(vector1.components, vector2.components)
        )
        return Vector2D(*new_components)

    def _add_scalar_with_vector(self, scalar: Scalar2D, vector: Vector2D):
        return Element2D(scalar, vector)

    def _add_element_with_scalar(self, element: Element2D, scalar: Scalar2D):
        return Element2D(element.scalar + scalar, element.vector)

    def _add_element_with_vector(self, element: Element2D, vector: Scalar2D):
        new_vector = self._add_vectors(element.vector, vector)
        return Element2D(element.scalar, new_vector)

    def _add_elements(self, element1: Element2D, element2: Element2D):
        new_scalar = self._add_scalars(element1.scalar, element2.scalar)
        new_vector = self._add_vectors(element1.vector, element2.vector)
        return Element2D(new_scalar, new_vector)
