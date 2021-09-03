import pytest
from pytest import approx
from implementation.space2d import Scalar2D, Vector2D, Element2D


@pytest.mark.parametrize('scalar1,scalar2,expected_result', [
    (0, 0, 0),
    (1, 3, 4),
    (1.5, 0.2, 1.7),
    (2, -0.5, 1.5),
    (2, -2.5, -0.5),
    (-1.2, -2.5, -3.7),
])
def test_add_scalars(scalar1, scalar2, expected_result, adder):
    s1 = Scalar2D(scalar1)
    s2 = Scalar2D(scalar2)
    resultado = adder.add(s1, s2)
    assert isinstance(resultado, Scalar2D)
    assert resultado == approx(expected_result)


@pytest.mark.parametrize('vector1,vector2,expected_result', [
    ((0, 0), (0, 0), (0, 0)),
    ((1, 2), (2, 4), (3, 6)),
    ((1.5, -1), (0, 2.2), (1.5, 1.2)),
    ((-2.1, 1.1), (-3.2, 2.2), (-5.3, 3.3)),
])
def test_add_vectors(vector1, vector2, expected_result, adder):
    v1 = Vector2D(vector1)
    v2 = Vector2D(vector2)
    resultado = adder.add(v1, v2)
    assert isinstance(resultado, Vector2D)
    assert resultado.x == approx(expected_result[0])
    assert resultado.y == approx(expected_result[1])


@pytest.mark.parametrize('scalar,vector', [
    (0, (0, 0)),
    (2.2, (2.1, -4.4)),
    (-1.1, (0, 2.2)),
])
def test_add_scalar_with_vector(scalar, vector, adder):
    s = Scalar2D(scalar)
    v = Vector2D(vector)
    resultado = adder.add(s, v)
    assert isinstance(resultado, Element2D)
    assert resultado.scalar == approx(scalar)
    assert resultado.vector.x == approx(vector[0])
    assert resultado.vector.y == approx(vector[1])


@pytest.mark.parametrize('element,scalar,expected_scalar_result', [
    ((0, 0, 0), 0, 0),
    ((2.1, -4.4, 1), -1.2, 0.9),
    ((-0.2, 9.2, 2.2), -1.1, -1.3),
])
def test_add_element_with_scalar(
    element, scalar, expected_scalar_result, adder
):
    e = Element2D(Scalar2D(element[0]), Vector2D(element[1], element[2]))
    s = Scalar2D(scalar)
    resultado = adder.add(e, s)
    assert isinstance(resultado, Element2D)
    assert resultado.scalar == approx(expected_scalar_result)
    assert resultado.vector.x == approx(element[1])
    assert resultado.vector.y == approx(element[2])


@pytest.mark.parametrize('element,vector,expected_vector_result', [
    ((0, 0, 0), (0, 0), (0, 0)),
    ((2.1, -4.4, 1), (-1.2, 1.9), (-5.6, 2.9)),
    ((-0.2, 9.2, 2.2), (-1.1, 0), (8.1, 2.2)),
])
def test_add_element_with_vector(element, vector, expected_vector_result, adder):
    e = Element2D(Scalar2D(element[0]), Vector2D(element[1], element[2]))
    v = Vector2D(vector)
    resultado = adder.add(e, v)
    assert isinstance(resultado, Element2D)
    assert resultado.scalar == approx(element[0])
    assert resultado.vector.x == approx(expected_vector_result[0])
    assert resultado.vector.y == approx(expected_vector_result[1])


@pytest.mark.parametrize('element1,element2,expected_result', [
    ((0, 0, 0), (0, 0, 0), (0, 0, 0)),
    ((2.1, -4.4, 1), (5.3, -1.2, 1.9), (7.4, -5.6, 2.9)),
    ((-0.2, 9.2, 2.2), (-1.1, 0, 2.6), (-1.3, 9.2, 4.8)),
])
def test_add_elements(element1, element2, expected_result, adder):
    e1 = Element2D(Scalar2D(element1[0]), Vector2D(element1[1], element1[2]))
    e2 = Element2D(Scalar2D(element2[0]), Vector2D(element2[1], element2[2]))
    resultado = adder.add(e1, e2)
    assert isinstance(resultado, Element2D)
    assert resultado.scalar == approx(expected_result[0])
    assert resultado.vector.x == approx(expected_result[1])
    assert resultado.vector.y == approx(expected_result[2])


def test_order_of_elements_doesnt_matter(adder):
    s1 = Scalar2D(4.3)
    s2 = Scalar2D(-3.3)
    v1 = Vector2D(14.8, 14.5)
    v2 = Vector2D(10.6, -4.5)
    e1 = Element2D(s1, v1)
    e2 = Element2D(s2, v2)

    assert adder.add(s1, s2) == adder.add(s2, s1)
    assert adder.add(v1, v2) == adder.add(v2, v1)
    assert adder.add(e1, e2) == adder.add(e2, e1)
    assert adder.add(s1, v2) == adder.add(v2, s1)
    assert adder.add(s1, e2) == adder.add(e2, s1)
    assert adder.add(v1, e2) == adder.add(e2, v1)
    