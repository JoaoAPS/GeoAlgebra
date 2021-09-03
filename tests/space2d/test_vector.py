import pytest
from pytest import approx
from src.implementation.space2d import Vector2D


@pytest.mark.parametrize('x,y', [(3.4, 1.5), (1, 1.5), (0, 0), (-3.4, 1.5)])
def test_creation_passing_components_separately(x, y):
    v = Vector2D(x, y)
    assert v.x == approx(x)
    assert v.y == approx(y)


@pytest.mark.parametrize('x,y', [('3.4', 1.5), (1.4, 'oi'), ([4], 0)])
def test_creation_error_passing_components_separately(x, y):
    with pytest.raises(TypeError):
        v = Vector2D(x, y)


@pytest.mark.parametrize('x,y', [(3.4, 1.5), (1, 1.5), (0, 0), (-3.4, 1.5)])
def test_creation_passing_tuple_successful(x, y):
    v = Vector2D((x, y))
    assert v.x == approx(x)
    assert v.y == approx(y)


@pytest.mark.parametrize('x,y', [('3.4', 1.5), (1.4, 'oi'), ([4], 0)])
def test_creation_errors_passing_tuple(x, y):
    with pytest.raises(TypeError):
        v = Vector2D((x, y))
    

def test_calculates_components_correctly():
    v = Vector2D(3.4, 1.5)
    components = v.components
    assert type(components) is tuple
    assert components[0] == approx(3.4)
    assert components[1] == approx(1.5)


def test_equality():
    v1 = Vector2D(1.2, 3)
    v2 = Vector2D(1.2, 3)
    v3 = Vector2D(1.1, 3)
    assert v1 == v2
    assert v1 != v3


@pytest.mark.parametrize('components,expected_modulus', [
    ((3, 4), 5),
    ((3, -4), 5),
    ((1.5, -2.5), 2.915475),
    ((4.2, 0), 4.2),
    ((0, 0), 0),
])
def test_modulus_is_calculated_correctly(components, expected_modulus):
    v = Vector2D(components)
    assert v.modulus == approx(expected_modulus)


def test_direction_is_calculated_correctly():
    pass


def test_direction_is_none_when_vector_is_null():
    pass
