import pytest

from domain.element import Element
from domain.scalar import Scalar
from domain.vector import Vector
from domain.bivector import Bivector


class TestElementCreation:

    def test_creation_via_grouped_components(self):
        s = Scalar(1.0)
        v = Vector(2.0, 3.0)
        bv = Bivector(4.0)
        e = Element(s, v, bv)

        assert e.scalar == s
        assert e.vector == v
        assert e.bivector == bv

    def test_creation_via_individual_components(self):
        e = Element(1.0, 2.0, 3.0, 4.0)
        assert e.scalar == 1.0
        assert e.vector == Vector(2.0, 3.0)
        assert e.bivector == Bivector(4.0)

    def test_creation_all_default_values(self):
        e = Element()
        assert e.scalar == Scalar()
        assert e.vector == Vector()
        assert e.bivector == Bivector()

    def test_creation_vector_and_bivector_default_value(self):
        e = Element(1.0)
        assert e.scalar == Scalar(1.0)
        assert e.vector == Vector()
        assert e.bivector == Bivector()

    def test_creation_bivector_default_value(self):
        e = Element(1.0, 2.0, 3.0)
        assert e.scalar == Scalar(1.0)
        assert e.vector == Vector(2.0, 3.0)
        assert e.bivector == Bivector()


class TestElementProperties:

    def test_calculates_components_correctly(self):
        e = Element(Scalar(1.0), Vector(2.0, 3.0), Bivector(4.0))
        assert e.scalar == 1.0
        assert e.vector == Vector(2.0, 3.0)
        assert e.bivector == Bivector(4.0)
        assert e.x == 2.0
        assert e.y == 3.0
        assert e.xy == 4.0

        components = e.components
        assert isinstance(components, tuple)
        assert len(components) == 4
        assert components == (1.0, 2.0, 3.0, 4.0)

    def test_cannot_change_components(self):
        e = Element(Scalar(1.0), Vector(2.0, 3.0), Bivector(4.0))
        with pytest.raises(AttributeError):
            e.scalar = 4.1
        with pytest.raises(AttributeError):
            e.vector = Vector(2.4, 1)
        with pytest.raises(AttributeError):
            e.bivector = Bivector(2.4)
        with pytest.raises(AttributeError):
            e.x = 4.1
        with pytest.raises(AttributeError):
            e.y = 4
        with pytest.raises(AttributeError):
            e.xy = 4.1
        with pytest.raises(AttributeError):
            e.components = (1, 3.4, 4.5, 1.3)

    def test_modulus_is_calculated_correctly(self):
        # TODO: Fazer quando eu souber calcular isso
        pass


def test_element_equality():
    v1 = Element(Scalar(1.0), Vector(2.0, 3.0), Bivector(4.0))
    v2 = Element(Scalar(1.0), Vector(2.0, 3.0), Bivector(4.0))
    v3 = Element(Scalar(77), Vector(2.0, 3.0), Bivector(4.0))
    v4 = Element(Scalar(1.0), Vector(77, 3.0), Bivector(4.0))
    v5 = Element(Scalar(1.0), Vector(2.0, 77), Bivector(4.0))
    v6 = Element(Scalar(1.0), Vector(2.0, 3.0), Bivector(77))
    assert v1 == v2
    assert v1 != v3
    assert v1 != v4
    assert v1 != v5
    assert v1 != v6
