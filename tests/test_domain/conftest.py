from pytest import fixture

from representation import ScalarData, VectorData, BivectorData
from domain import Scalar, Vector, Bivector, Element


@fixture
def scalar(fake_adder):
    return Scalar(ScalarData(1.2), fake_adder)


@fixture
def vector(fake_adder):
    return Vector(VectorData(2.2, -3.0), fake_adder)


@fixture
def bivector(fake_adder):
    return Bivector(BivectorData(4.4), fake_adder)


@fixture
def element(scalar, vector, bivector, fake_adder):
    return Element(scalar, vector, bivector, fake_adder)
