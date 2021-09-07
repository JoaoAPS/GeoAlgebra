from pytest import fixture
from factory.factory import Factory


@fixture
def factory():
    return Factory()
