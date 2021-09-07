from operations.abstract import AbstractAdd
from domain.abstract import (
    Entity, AbstractScalar, AbstractVector, AbstractBivector, AbstractElement)


class Add(AbstractAdd):

    def add(self, entity1: Entity, entity2: Entity):
        if isinstance(entity1, AbstractScalar):
            if isinstance(entity2, AbstractScalar):
                return self._add_scalars(entity1, entity2)
            if isinstance(entity2, AbstractVector):
                return self._add_scalar_with_vector(entity1, entity2)
            if isinstance(entity2, AbstractBivector):
                return self._add_scalar_with_bivector(entity1, entity2)
            if isinstance(entity2, AbstractElement):
                return self._add_element_with_scalar(entity2, entity1)

        if isinstance(entity1, AbstractVector):
            if isinstance(entity2, AbstractScalar):
                return self._add_scalar_with_vector(entity2, entity1)
            if isinstance(entity2, AbstractVector):
                return self._add_vectors(entity1, entity2)
            if isinstance(entity2, AbstractBivector):
                return self._add_vector_with_bivector(entity1, entity2)
            if isinstance(entity2, AbstractElement):
                return self._add_element_with_vector(entity2, entity1)

        if isinstance(entity1, AbstractBivector):
            if isinstance(entity2, AbstractScalar):
                return self._add_scalar_with_bivector(entity2, entity1)
            if isinstance(entity2, AbstractVector):
                return self._add_vector_with_bivector(entity2, entity1)
            if isinstance(entity2, AbstractBivector):
                return self._add_bivectors(entity1, entity2)
            if isinstance(entity2, AbstractElement):
                return self._add_element_with_bivector(entity2, entity1)

        if isinstance(entity1, AbstractElement):
            if isinstance(entity2, AbstractScalar):
                return self._add_element_with_scalar(entity1, entity2)
            if isinstance(entity2, AbstractVector):
                return self._add_element_with_vector(entity1, entity2)
            if isinstance(entity2, AbstractBivector):
                return self._add_element_with_bivector(entity1, entity2)
            if isinstance(entity2, AbstractElement):
                return self._add_elements(entity1, entity2)

        raise TypeError(f'Cannot add {type(entity1)} with {type(entity2)}')

    def _add_scalars(self, scalar1: AbstractScalar, scalar2: AbstractScalar):
        return self.factory.scalar(float(scalar1) + float(scalar2))

    def _add_vectors(self, vector1: AbstractVector, vector2: AbstractVector):
        new_components = (
            v1_comp + v2_comp
            for v1_comp, v2_comp in zip(vector1.components, vector2.components)
        )
        return self.factory.vector(*new_components)

    def _add_bivectors(
        self, bivector1: AbstractBivector, bivector2: AbstractBivector
    ):
        new_components = (
            bv1_comp + bv2_comp for bv1_comp, bv2_comp
            in zip(bivector1.components, bivector2.components)
        )
        return self.factory.bivector(*new_components)

    def _add_elements(
        self, element1: AbstractElement, element2: AbstractElement
    ):
        new_scalar = self._add_scalars(element1.scalar, element2.scalar)
        new_vector = self._add_vectors(element1.vector, element2.vector)
        new_bivector = self._add_bivectors(
            element1.bivector, element2.bivector)
        return self.factory.element(new_scalar, new_vector, new_bivector)

    def _add_scalar_with_vector(
        self, scalar: AbstractScalar, vector: AbstractVector
    ):
        return self.factory.element(scalar, vector)

    def _add_scalar_with_bivector(
        self, scalar: AbstractScalar, bivector: AbstractBivector
    ):
        return self.factory.element(scalar, y_or_bivector=bivector)

    def _add_vector_with_bivector(
        self, vector: AbstractVector, bivector: AbstractBivector
    ):
        return self.factory.element(0, vector, bivector)


    def _add_element_with_scalar(
        self, element: AbstractElement, scalar: AbstractScalar
    ):
        new_scalar = self._add_scalars(element.scalar, scalar)
        return self.factory.element(
            new_scalar, element.vector, element.bivector)

    def _add_element_with_vector(
        self, element: AbstractElement, vector: AbstractVector
    ):
        new_vector = self._add_vectors(element.vector, vector)
        return self.factory.element(
            element.scalar, new_vector, element.bivector)

    def _add_element_with_bivector(
        self, element: AbstractElement, bivector: AbstractBivector
    ):
        new_bivector = self._add_bivectors(element.bivector, bivector)
        return self.factory.element(
            element.scalar, element.vector, new_bivector)
