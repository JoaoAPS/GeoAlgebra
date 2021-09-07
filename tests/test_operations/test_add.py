import pytest
from pytest import approx

from domain.scalar import Scalar
from domain.vector import Vector
from domain.bivector import Bivector
from domain.element import Element


@pytest.mark.parametrize('scalar1,scalar2,expected_result', [
    (0, 0, 0),
    (1, 3, 4),
    (1.5, 0.2, 1.7),
    (2, -0.5, 1.5),
    (2, -2.5, -0.5),
    (-1.2, -2.5, -3.7),
])
def test_add_scalars(scalar1, scalar2, expected_result, adder):
    s1 = Scalar(scalar1)
    s2 = Scalar(scalar2)
    resultado = adder.add(s1, s2)
    assert isinstance(resultado, Scalar)
    assert float(resultado) == approx(expected_result)


@pytest.mark.parametrize('vector1,vector2,expected_result', [
    ((0, 0), (0, 0), (0, 0)),
    ((1, 2), (2, 4), (3, 6)),
    ((1.5, -1), (0, 2.2), (1.5, 1.2)),
    ((-2.1, 1.1), (-3.2, 2.2), (-5.3, 3.3)),
])
def test_add_vectors(vector1, vector2, expected_result, adder):
    v1 = Vector(vector1)
    v2 = Vector(vector2)
    resultado = adder.add(v1, v2)
    assert isinstance(resultado, Vector)
    assert resultado.x == approx(expected_result[0])
    assert resultado.y == approx(expected_result[1])


@pytest.mark.parametrize('bivector1,bivector2,expected_result', [
    (0, 0, 0),
    (1, 2, 3),
    (-1.4, 2.2, 0.8),
    (1.1, -3.2, -2.1),
])
def test_add_bivectors(bivector1, bivector2, expected_result, adder):
    bv1 = Bivector(bivector1)
    bv2 = Bivector(bivector2)
    resultado = adder.add(bv1, bv2)
    assert isinstance(resultado, Bivector)
    assert resultado.xy == approx(expected_result)


@pytest.mark.parametrize('element1,element2,expected_result', [
    ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
    ((2.1, -4.4, 1, 0.1), (5.3, -1.2, 1.9, -0.1), (7.4, -5.6, 2.9, 0)),
    ((-0.2, 9.2, 2.2, 10.2), (-1.1, 0, 2.6, 1.2), (-1.3, 9.2, 4.8, 11.4)),
])
def test_add_elements(element1, element2, expected_result, adder):
    e1 = Element(
        Scalar(element1[0]),
        Vector(element1[1], element1[2]),
        Bivector(element1[3])
    )
    e2 = Element(
        Scalar(element2[0]),
        Vector(element2[1], element2[2]),
        Bivector(element2[3])
    )
    resultado = adder.add(e1, e2)
    assert isinstance(resultado, Element)
    assert float(resultado.scalar) == approx(expected_result[0])
    assert resultado.x == approx(expected_result[1])
    assert resultado.y == approx(expected_result[2])
    assert resultado.xy == approx(expected_result[3])


@pytest.mark.parametrize('scalar,vector', [
    (0, (0, 0)),
    (2.2, (2.1, -4.4)),
    (-1.1, (0, 2.2)),
])
def test_add_scalar_with_vector(scalar, vector, adder):
    s = Scalar(scalar)
    v = Vector(vector)
    resultado = adder.add(s, v)
    assert isinstance(resultado, Element)
    assert float(resultado.scalar) == approx(scalar)
    assert resultado.vector.x == approx(vector[0])
    assert resultado.vector.y == approx(vector[1])


@pytest.mark.parametrize('scalar,bivector', [
    (0, 0),
    (2.2, -4.4),
    (-1.1, 7.1),
])
def test_add_scalar_with_bivector(scalar, bivector, adder):
    s = Scalar(scalar)
    bv = Bivector(bivector)
    resultado = adder.add(s, bv)
    assert isinstance(resultado, Element)
    assert float(resultado.scalar) == approx(scalar)
    assert resultado.x == approx(0)
    assert resultado.y == approx(0)
    assert resultado.xy == approx(bivector)


@pytest.mark.parametrize('element,scalar,expected_scalar_result', [
    ((0, 0, 0, 0), 0, 0),
    ((2.1, -4.4, 1, 0.4), -1.2, 0.9),
    ((-0.2, 9.2, 2.2, 10), -1.1, -1.3),
])
def test_add_element_with_scalar(
    element, scalar, expected_scalar_result, adder
):
    e = Element(
        Scalar(element[0]),
        Vector(element[1], element[2]),
        Bivector(element[3])
    )
    s = Scalar(scalar)
    resultado = adder.add(e, s)
    assert isinstance(resultado, Element)
    assert float(resultado.scalar) == approx(expected_scalar_result)
    assert resultado.x == approx(element[1])
    assert resultado.y == approx(element[2])
    assert resultado.xy == approx(element[3])


@pytest.mark.parametrize('vector,bivector', [
    ((0, 5.4), 0),
    ((2.2, 9.9), -4.4),
    ((-1.1, 0), 8.1),
])
def test_add_vector_with_bivector(vector, bivector, adder):
    v = Vector(vector)
    bv = Bivector(bivector)
    resultado = adder.add(v, bv)
    assert isinstance(resultado, Element)
    assert float(resultado.scalar) == approx(0)
    assert resultado.x == approx(vector[0])
    assert resultado.y == approx(vector[1])
    assert resultado.xy == approx(bivector)


@pytest.mark.parametrize('element,vector,expected_vector_result', [
    ((0, 0, 0, 0), (0, 0), (0, 0)),
    ((2.1, -4.4, 1, 6), (-1.2, 1.9), (-5.6, 2.9)),
    ((-0.2, 9.2, 2.2, 8.7), (-1.1, 0), (8.1, 2.2)),
])
def test_add_element_with_vector(
    element, vector, expected_vector_result, adder
):
    e = Element(
        Scalar(element[0]),
        Vector(element[1], element[2]),
        Bivector(element[3])
    )
    v = Vector(vector)
    resultado = adder.add(e, v)
    assert isinstance(resultado, Element)
    assert float(resultado.scalar) == approx(element[0])
    assert resultado.x == approx(expected_vector_result[0])
    assert resultado.y == approx(expected_vector_result[1])
    assert resultado.xy == approx(element[3])


@pytest.mark.parametrize('element,bivector,expected_bivector_result', [
    ((0, 0, 0, 0), 0, 0),
    ((2.1, -4.4, 1, 1.4), -1.2, 0.2),
    ((-0.2, 9.2, 2.2, 6.5), 1.3, 7.8),
])
def test_add_element_with_bivector(
    element, bivector, expected_bivector_result, adder
):
    e = Element(
        Scalar(element[0]),
        Vector(element[1], element[2]),
        Bivector(element[3])
    )
    bv = Bivector(bivector)
    resultado = adder.add(e, bv)
    assert isinstance(resultado, Element)
    assert float(resultado.scalar) == approx(element[0])
    assert resultado.x == approx(element[1])
    assert resultado.y == approx(element[2])
    assert resultado.xy == approx(expected_bivector_result)


def test_order_of_elements_doesnt_matter(adder):
    s1 = Scalar(4.3)
    s2 = Scalar(-3.3)
    v1 = Vector(14.8, 14.5)
    v2 = Vector(10.6, -4.5)
    bv1 = Bivector(4.8)
    bv2 = Bivector(-1.6)
    e1 = Element(s1, v1)
    e2 = Element(s2, v2)

    assert adder.add(s1, s2) == adder.add(s2, s1)
    assert adder.add(v1, v2) == adder.add(v2, v1)
    assert adder.add(bv1, bv2) == adder.add(bv2, bv1)
    assert adder.add(e1, e2) == adder.add(e2, e1)

    assert adder.add(s1, v2) == adder.add(v2, s1)
    assert adder.add(s1, bv2) == adder.add(bv2, s1)
    assert adder.add(s1, e2) == adder.add(e2, s1)
    assert adder.add(v1, bv2) == adder.add(bv2, v1)
    assert adder.add(v1, e2) == adder.add(e2, v1)
    assert adder.add(bv1, e2) == adder.add(e2, bv1)
