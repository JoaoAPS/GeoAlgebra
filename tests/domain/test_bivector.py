import pytest
from pytest import approx

from domain.bivector import Bivector


class TestBivectorCreation:

    def test_creation_default_value(self):
        bv = Bivector()
        assert bv.xy == approx(0)

    @pytest.mark.parametrize('xy', [3, 0, -3.4, 1.5])
    def test_creation_successful(self, xy):
        bv = Bivector(xy)
        assert isinstance(bv.xy, float)
        assert bv.xy == approx(xy)

    @pytest.mark.parametrize('xy', ['3.4', 'oi', [4], False])
    def test_creation_errors(self, xy):
        with pytest.raises(TypeError):
            Bivector(xy)


class TestBivectorProperties:

    def test_cannot_change_components(self):
        bv = Bivector(1.3)
        with pytest.raises(AttributeError):
            bv.xy = 4.1
        with pytest.raises(AttributeError):
            bv.components = (3.4)

    def test_calculates_components_correctly(self):
        bv = Bivector(1.5)
        components = bv.components
        assert isinstance(components, tuple)
        assert len(components) == 1
        assert components[0] == approx(1.5)

    @pytest.mark.parametrize('xy,expected_modulus', [
        (3, 3),
        (-4.2, 4.2),
        (0, 0)
    ])
    def test_modulus_is_calculated_correctly(self, xy, expected_modulus):
        bv = Bivector(xy)
        assert bv.modulus == approx(expected_modulus)

    def test_direction_is_calculated_correctly(self):
        pass

    def test_direction_is_none_when_vector_is_null(self):
        pass


def test_bivector_equality():
    bv1 = Bivector(1.2)
    bv2 = Bivector(1.2)
    bv3 = Bivector(1.1)
    assert bv1 == bv2
    assert bv1 != bv3
