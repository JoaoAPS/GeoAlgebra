from pytest import fixture
from factory.factory import Factory


@fixture
def factory():
    return Factory()


@fixture
def scalar(factory):
    return factory.make_scalar(1)


@fixture
def vector(factory):
    return factory.make_vector(2, 3)


@fixture
def bivector(factory):
    return factory.make_bivector(4)
