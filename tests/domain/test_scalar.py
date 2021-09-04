from pytest import approx
from domain.scalar import Scalar


def test_creation_with_value():
    s = Scalar(4.5)
    assert s.value == approx(4.5)


def test_creation_deafult_value():
    s = Scalar()
    assert s.value == approx(0)


def test_float_equivalence():
    s = Scalar(1.0)
    assert float(s) == approx(1.0)
