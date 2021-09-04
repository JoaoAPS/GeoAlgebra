import pytest
from pytest import approx
from domain.scalar import Scalar


class TestScalarCreation:
    
    def test_creation_with_value(self):
        s = Scalar(4.5)
        assert s.value == approx(4.5)

    def test_creation_deafult_value(self):
        s = Scalar()
        assert s.value == approx(0)

    @pytest.mark.parametrize('value', ['12', 'oi', [1], False])
    def test_creation_raises_error_if_value_is_not_number(self, value):
        with pytest.raises(TypeError):
            Scalar(value)


def test_float_equivalence():
    s = Scalar(1.0)
    assert float(s) == approx(1.0)


def test_scalar_is_immutable():
    s = Scalar(1)
    with pytest.raises(AttributeError):
        s.value = 2

def test_equality_with_other_scalars():
    s1 = Scalar(2.0)
    s2 = Scalar(2.0)
    s3 = Scalar(2.5)
    assert s1 == s2
    assert s1 != s3

def test_equality_with_numbers():
    s1 = Scalar(2.0)
    assert s1 == 2.0
    assert s1 != 3.1
