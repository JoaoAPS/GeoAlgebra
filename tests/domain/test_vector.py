import pytest
from pytest import approx

from domain.vector import Vector


class TestVectorCreation:

    def test_creation_default_value(self):
        v = Vector()
        assert v.x == approx(0)
        assert v.y == approx(0)

    @pytest.mark.parametrize('x,y', [(3, 1), (0, 0), (-3.4, 1.5)])
    def test_creation_passing_components_separately_successful(self, x, y):
        v = Vector(x, y)
        assert isinstance(v.x, float)
        assert isinstance(v.y, float)
        assert v.x == approx(x)
        assert v.y == approx(y)

    @pytest.mark.parametrize('x,y', [('3.4', 1.5), (1.4, 'oi'), ([4], 0)])
    def test_creation_error_passing_components_separately(self, x, y):
        with pytest.raises(TypeError):
            Vector(x, y)

    @pytest.mark.parametrize('x,y', [(1, 5), (0, 0), (-3.4, 1.5)])
    def test_creation_passing_tuple_successful(self, x, y):
        v = Vector((x, y))
        assert isinstance(v.x, float)
        assert isinstance(v.y, float)
        assert v.x == approx(x)
        assert v.y == approx(y)


    @pytest.mark.parametrize('x,y', [('3.4', 1.5), (1.4, 'oi'), ([4], 0)])
    def test_creation_errors_passing_tuple(self, x, y):
        with pytest.raises(TypeError):
            Vector((x, y))


class TestVectorProperties:

    def test_cannot_change_components(self):
        v = Vector(1, 3)
        with pytest.raises(AttributeError):
            v.x = 4.1
        with pytest.raises(AttributeError):
            v.y = 4
        with pytest.raises(AttributeError):
            v.components = (1, 3.4)

    def test_calculates_components_correctly(self):
        v = Vector(3.4, 1.5)
        components = v.components
        assert isinstance(components, tuple)
        assert components[0] == approx(3.4)
        assert components[1] == approx(1.5)

    @pytest.mark.parametrize('components,expected_modulus', [
        ((3, 4), 5),
        ((3, -4), 5),
        ((1.5, -2.5), 2.915475),
        ((4.2, 0), 4.2),
        ((0, 0), 0),
    ])
    def test_modulus_is_calculated_correctly(
        self, components, expected_modulus
    ):
        v = Vector(components)
        assert v.modulus == approx(expected_modulus)


    def test_direction_is_calculated_correctly(self):
        pass


    def test_direction_is_none_when_vector_is_null(self):
        pass



def test_equality():
    v1 = Vector(1.2, 3)
    v2 = Vector(1.2, 3)
    v3 = Vector(1.1, 3)
    assert v1 == v2
    assert v1 != v3
