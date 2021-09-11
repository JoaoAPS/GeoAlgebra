import pytest
from pytest import approx

from domain.scalar import Scalar


class TestScalarCreation:

    def test_creation_with_value(self, factory):
        s = factory.make_scalar(4.5)
        assert isinstance(s, Scalar)
        assert s.value == approx(4.5)

    def test_creation_deafult_value(self, factory):
        s = factory.make_scalar()
        assert isinstance(s, Scalar)
        assert s.value == approx(0)

    def test_creation_from_another_scalar(self, factory):
        s0 = factory.make_scalar(2.5)
        s = factory.make_scalar(s0)
        assert isinstance(s, Scalar)
        assert s.value == approx(2.5)

    @pytest.mark.parametrize('value', ['12', 'oi', [1], False])
    def test_creation_raises_error_if_value_is_not_number(
        self, value, factory
    ):
        with pytest.raises(TypeError):
            factory.make_scalar(value)
