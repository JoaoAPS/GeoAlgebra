import pytest
from pytest import approx
from src.implementation.space2d import Element2D, Scalar2D, Vector2D


def test_equality():
    e1 = Element2D(Scalar2D(0.2), Vector2D(1.2, 3))
    e2 = Element2D(Scalar2D(0.2), Vector2D(1.2, 3))
    e3 = Element2D(Scalar2D(0.4), Vector2D(1.2, 3))
    e4 = Element2D(Scalar2D(0.2), Vector2D(1.2, 5))
    e5 = Element2D(Scalar2D(1.0), Vector2D(1.1, 3))

    assert e1 == e2
    assert e1 != e3
    assert e1 != e4
    assert e1 != e5
