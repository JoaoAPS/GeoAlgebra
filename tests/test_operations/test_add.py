import pytest
from pytest import approx

from representation.scalar import ScalarData
from domain.scalar import Scalar
# from domain.vector import Vector
# from domain.bivector import Bivector
# from domain.element import Element


@pytest.mark.parametrize('scalar1,scalar2,expected_result', [
    (0, 0, 0),
    (1, 3, 4),
    (1.5, 0.2, 1.7),
    (2, -0.5, 1.5),
    (2, -2.5, -0.5),
    (-1.2, -2.5, -3.7),
])
def test_add_scalars(scalar1, scalar2, expected_result, adder):
    s1 = Scalar(ScalarData(scalar1), adder)
    s2 = Scalar(ScalarData(scalar2), adder)
    result = adder.add(s1, s2)
    assert isinstance(result, Scalar)
    assert result.value == approx(expected_result)


@pytest.mark.parametrize('scalar,number,expected_result', [
    (0, 0, 0),
    (1.5, 0.2, 1.7),
    (2, -0.5, 1.5),
])
def test_add_scalar_with_number(scalar, number, expected_result, adder):
    s = Scalar(ScalarData(scalar), adder)
    result = adder.add(s, number)
    assert isinstance(result, Scalar)
    assert result.value == approx(expected_result)

    result_switched = adder.add(number, s)
    assert isinstance(result_switched, Scalar)
    assert result_switched.value == approx(expected_result)



# @pytest.mark.parametrize('vector1,vector2,expected_result', [
#     ((0, 0), (0, 0), (0, 0)),
#     ((1, 2), (2, 4), (3, 6)),
#     ((1.5, -1), (0, 2.2), (1.5, 1.2)),
#     ((-2.1, 1.1), (-3.2, 2.2), (-5.3, 3.3)),
# ])
# def test_add_vectors(vector1, vector2, expected_result, adder):
#     v1 = Vector(vector1)
#     v2 = Vector(vector2)
#     result = adder.add(v1, v2)
#     assert isinstance(result, Vector)
#     assert result.x == approx(expected_result[0])
#     assert result.y == approx(expected_result[1])


# @pytest.mark.parametrize('bivector1,bivector2,expected_result', [
#     (0, 0, 0),
#     (1, 2, 3),
#     (-1.4, 2.2, 0.8),
#     (1.1, -3.2, -2.1),
# ])
# def test_add_bivectors(bivector1, bivector2, expected_result, adder):
#     bv1 = Bivector(bivector1)
#     bv2 = Bivector(bivector2)
#     result = adder.add(bv1, bv2)
#     assert isinstance(result, Bivector)
#     assert result.xy == approx(expected_result)


# @pytest.mark.parametrize('element1,element2,expected_result', [
#     ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
#     ((2.1, -4.4, 1, 0.1), (5.3, -1.2, 1.9, -0.1), (7.4, -5.6, 2.9, 0)),
#     ((-0.2, 9.2, 2.2, 10.2), (-1.1, 0, 2.6, 1.2), (-1.3, 9.2, 4.8, 11.4)),
# ])
# def test_add_elements(element1, element2, expected_result, adder):
#     e1 = Element(
#         Scalar(element1[0]),
#         Vector(element1[1], element1[2]),
#         Bivector(element1[3])
#     )
#     e2 = Element(
#         Scalar(element2[0]),
#         Vector(element2[1], element2[2]),
#         Bivector(element2[3])
#     )
#     result = adder.add(e1, e2)
#     assert isinstance(result, Element)
#     assert float(result.scalar) == approx(expected_result[0])
#     assert result.x == approx(expected_result[1])
#     assert result.y == approx(expected_result[2])
#     assert result.xy == approx(expected_result[3])


# @pytest.mark.parametrize('scalar,vector', [
#     (0, (0, 0)),
#     (2.2, (2.1, -4.4)),
#     (-1.1, (0, 2.2)),
# ])
# def test_add_scalar_with_vector(scalar, vector, adder):
#     s = Scalar(scalar)
#     v = Vector(vector)
#     result = adder.add(s, v)
#     assert isinstance(result, Element)
#     assert float(result.scalar) == approx(scalar)
#     assert result.vector.x == approx(vector[0])
#     assert result.vector.y == approx(vector[1])


# @pytest.mark.parametrize('scalar,bivector', [
#     (0, 0),
#     (2.2, -4.4),
#     (-1.1, 7.1),
# ])
# def test_add_scalar_with_bivector(scalar, bivector, adder):
#     s = Scalar(scalar)
#     bv = Bivector(bivector)
#     result = adder.add(s, bv)
#     assert isinstance(result, Element)
#     assert float(result.scalar) == approx(scalar)
#     assert result.x == approx(0)
#     assert result.y == approx(0)
#     assert result.xy == approx(bivector)


# @pytest.mark.parametrize('element,scalar,expected_scalar_result', [
#     ((0, 0, 0, 0), 0, 0),
#     ((2.1, -4.4, 1, 0.4), -1.2, 0.9),
#     ((-0.2, 9.2, 2.2, 10), -1.1, -1.3),
# ])
# def test_add_element_with_scalar(
#     element, scalar, expected_scalar_result, adder
# ):
#     e = Element(
#         Scalar(element[0]),
#         Vector(element[1], element[2]),
#         Bivector(element[3])
#     )
#     s = Scalar(scalar)
#     result = adder.add(e, s)
#     assert isinstance(result, Element)
#     assert float(result.scalar) == approx(expected_scalar_result)
#     assert result.x == approx(element[1])
#     assert result.y == approx(element[2])
#     assert result.xy == approx(element[3])


# @pytest.mark.parametrize('vector,bivector', [
#     ((0, 5.4), 0),
#     ((2.2, 9.9), -4.4),
#     ((-1.1, 0), 8.1),
# ])
# def test_add_vector_with_bivector(vector, bivector, adder):
#     v = Vector(vector)
#     bv = Bivector(bivector)
#     result = adder.add(v, bv)
#     assert isinstance(result, Element)
#     assert float(result.scalar) == approx(0)
#     assert result.x == approx(vector[0])
#     assert result.y == approx(vector[1])
#     assert result.xy == approx(bivector)


# @pytest.mark.parametrize('element,vector,expected_vector_result', [
#     ((0, 0, 0, 0), (0, 0), (0, 0)),
#     ((2.1, -4.4, 1, 6), (-1.2, 1.9), (-5.6, 2.9)),
#     ((-0.2, 9.2, 2.2, 8.7), (-1.1, 0), (8.1, 2.2)),
# ])
# def test_add_element_with_vector(
#     element, vector, expected_vector_result, adder
# ):
#     e = Element(
#         Scalar(element[0]),
#         Vector(element[1], element[2]),
#         Bivector(element[3])
#     )
#     v = Vector(vector)
#     result = adder.add(e, v)
#     assert isinstance(result, Element)
#     assert float(result.scalar) == approx(element[0])
#     assert result.x == approx(expected_vector_result[0])
#     assert result.y == approx(expected_vector_result[1])
#     assert result.xy == approx(element[3])


# @pytest.mark.parametrize('element,bivector,expected_bivector_result', [
#     ((0, 0, 0, 0), 0, 0),
#     ((2.1, -4.4, 1, 1.4), -1.2, 0.2),
#     ((-0.2, 9.2, 2.2, 6.5), 1.3, 7.8),
# ])
# def test_add_element_with_bivector(
#     element, bivector, expected_bivector_result, adder
# ):
#     e = Element(
#         Scalar(element[0]),
#         Vector(element[1], element[2]),
#         Bivector(element[3])
#     )
#     bv = Bivector(bivector)
#     result = adder.add(e, bv)
#     assert isinstance(result, Element)
#     assert float(result.scalar) == approx(element[0])
#     assert result.x == approx(element[1])
#     assert result.y == approx(element[2])
#     assert result.xy == approx(expected_bivector_result)


# def test_order_of_elements_doesnt_matter(adder):
#     s1 = Scalar(4.3)
#     s2 = Scalar(-3.3)
#     v1 = Vector(14.8, 14.5)
#     v2 = Vector(10.6, -4.5)
#     bv1 = Bivector(4.8)
#     bv2 = Bivector(-1.6)
#     e1 = Element(s1, v1)
#     e2 = Element(s2, v2)

#     assert adder.add(s1, s2) == adder.add(s2, s1)
#     assert adder.add(v1, v2) == adder.add(v2, v1)
#     assert adder.add(bv1, bv2) == adder.add(bv2, bv1)
#     assert adder.add(e1, e2) == adder.add(e2, e1)

#     assert adder.add(s1, v2) == adder.add(v2, s1)
#     assert adder.add(s1, bv2) == adder.add(bv2, s1)
#     assert adder.add(s1, e2) == adder.add(e2, s1)
#     assert adder.add(v1, bv2) == adder.add(bv2, v1)
#     assert adder.add(v1, e2) == adder.add(e2, v1)
#     assert adder.add(bv1, e2) == adder.add(e2, bv1)
