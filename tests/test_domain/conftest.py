from pytest import fixture

from representation import ScalarData, VectorData, BivectorData
from domain import Scalar, Vector, Bivector, Element


@fixture
def scalar(fake_operator):
    return Scalar(ScalarData(1.2), fake_operator)


@fixture
def vector(fake_operator):
    return Vector(VectorData(2.2, -3.0), fake_operator)


@fixture
def bivector(fake_operator):
    return Bivector(BivectorData(4.4), fake_operator)


@fixture
def element(scalar, vector, bivector, fake_operator):
    return Element(scalar, vector, bivector, fake_operator)
