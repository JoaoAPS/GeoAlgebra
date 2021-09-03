from pytest import fixture

from implementation.space2d import Adder2D


@fixture
def adder():
    return Adder2D()
