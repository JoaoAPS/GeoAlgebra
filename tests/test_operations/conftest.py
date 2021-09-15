from pytest import fixture
from factory.factory import Factory
from operations.add import Add


@fixture
def adder():
    factory = Factory()
    return Add(factory)


@fixture
def factory():
    return Factory()
