from pytest import fixture
from factory.factory import Factory
from operations.add import Adder


@fixture
def adder():
    factory = Factory()
    return Adder(factory)


@fixture
def factory():
    return Factory()
