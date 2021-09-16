from numbers import Number

from abstraction.operations import AbstractAdder
from abstraction.domain import Entity
from abstraction.factory import AbstractFactory
from domain import Scalar, Vector, Bivector, Element


class Adder(AbstractAdder):

    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    def add(self, entity1: Entity, entity2: Entity) -> Entity:
        entity1, entity2 = self._transform_number_to_scalar(entity1, entity2)

        if isinstance(entity1, Scalar):
            if isinstance(entity2, Scalar):
                return self._add_scalars(entity1, entity2)
            if isinstance(entity2, Vector):
                return self._add_scalar_with_vector(entity1, entity2)
            if isinstance(entity2, Bivector):
                return self._add_scalar_with_bivector(entity1, entity2)
            if isinstance(entity2, Element):
                return self._add_element_with_scalar(entity2, entity1)

        if isinstance(entity1, Vector):
            if isinstance(entity2, Scalar):
                return self._add_scalar_with_vector(entity2, entity1)
            if isinstance(entity2, Vector):
                return self._add_vectors(entity1, entity2)
            if isinstance(entity2, Bivector):
                return self._add_vector_with_bivector(entity1, entity2)
            if isinstance(entity2, Element):
                return self._add_element_with_vector(entity2, entity1)

        if isinstance(entity1, Bivector):
            if isinstance(entity2, Scalar):
                return self._add_scalar_with_bivector(entity2, entity1)
            if isinstance(entity2, Vector):
                return self._add_vector_with_bivector(entity2, entity1)
            if isinstance(entity2, Bivector):
                return self._add_bivectors(entity1, entity2)
            if isinstance(entity2, Element):
                return self._add_element_with_bivector(entity2, entity1)

        if isinstance(entity1, Element):
            if isinstance(entity2, Scalar):
                return self._add_element_with_scalar(entity1, entity2)
            if isinstance(entity2, Vector):
                return self._add_element_with_vector(entity1, entity2)
            if isinstance(entity2, Bivector):
                return self._add_element_with_bivector(entity1, entity2)
            if isinstance(entity2, Element):
                return self._add_elements(entity1, entity2)

        raise TypeError(f'Cannot add {type(entity1)} with {type(entity2)}')

    def _transform_number_to_scalar(self, entity1, entity2):
        if isinstance(entity1, Number) and not isinstance(entity1, bool):
            entity1 = self.factory.make_scalar(entity1)
        if isinstance(entity2, Number) and not isinstance(entity2, bool):
            entity2 = self.factory.make_scalar(entity2)
        return entity1, entity2

    def _add_scalars(self, scalar1: Scalar, scalar2: Scalar):
        result_value = scalar1.value + scalar2.value
        return self.factory.make_scalar(result_value)

    def _add_vectors(self, vector1: Vector, vector2: Vector):
        new_components = (
            v1_comp + v2_comp for v1_comp, v2_comp
            in zip(vector1.components, vector2.components)
        )
        return self.factory.make_vector(*new_components)

    def _add_bivectors(self, bivector1: Bivector, bivector2: Bivector):
        new_components = (
            bv1_comp + bv2_comp for bv1_comp, bv2_comp
            in zip(bivector1.components, bivector2.components)
        )
        return self.factory.make_bivector(*new_components)

    def _add_elements(self, element1: Element, element2: Element):
        new_scalar = self._add_scalars(element1.scalar, element2.scalar)
        new_vector = self._add_vectors(element1.vector, element2.vector)
        new_bivector = self._add_bivectors(
            element1.bivector, element2.bivector)
        return self.factory.make_element(new_scalar, new_vector, new_bivector)

    def _add_scalar_with_vector(self, scalar: Scalar, vector: Vector):
        return self.factory.make_element(scalar=scalar, vector=vector)

    def _add_scalar_with_bivector(self, scalar: Scalar, bivector: Bivector):
        return self.factory.make_element(scalar=scalar, bivector=bivector)

    def _add_vector_with_bivector(self, vector: Vector, bivector: Bivector):
        return self.factory.make_element(vector=vector, bivector=bivector)

    def _add_element_with_scalar(self, element: Element, scalar: Scalar):
        new_scalar = self._add_scalars(element.scalar, scalar)
        return self.factory.make_element(
            new_scalar, element.vector, element.bivector)

    def _add_element_with_vector(self, element: Element, vector: Vector):
        new_vector = self._add_vectors(element.vector, vector)
        return self.factory.make_element(
            element.scalar, new_vector, element.bivector)

    def _add_element_with_bivector(self, element: Element, bivector: Bivector):
        new_bivector = self._add_bivectors(element.bivector, bivector)
        return self.factory.make_element(
            element.scalar, element.vector, new_bivector)
