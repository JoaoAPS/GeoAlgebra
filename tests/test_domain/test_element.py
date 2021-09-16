import pytest
from pytest import approx

from representation import ScalarData, VectorData, BivectorData
from domain import Scalar, Vector, Bivector, Element


class TestElementInitialization:

    def test_initialization_successful(self, fake_operator):
        s = Scalar(ScalarData(0.5), fake_operator)
        v = Vector(VectorData(1.2, -0.2), fake_operator)
        bv = Bivector(BivectorData(7.0), fake_operator)
        e = Element(s, v, bv, fake_operator)

        assert e._scalar == s
        assert e._vector == v
        assert e._bivector == bv
        assert e._operator == fake_operator

    def test_initialization_wrong_scalar_type(
        self, vector, bivector, fake_operator
    ):
        s = 0.1
        with pytest.raises(TypeError):
            Element(s, vector, bivector, fake_operator)

    def test_initialization_wrong_vector_type(
        self, scalar, bivector, fake_operator
    ):
        v = (1.2, 3.2)
        with pytest.raises(TypeError):
            Element(scalar, v, bivector, fake_operator)

    def test_initialization_wrong_bivector_type(
        self, scalar, vector, fake_operator
    ):
        bv = 4.1
        with pytest.raises(TypeError):
            Element(scalar, vector, bv, fake_operator)

    def test_initialization_wrong_operator_type(
        self, scalar, vector, bivector, fake_operator
    ):
        with pytest.raises(TypeError):
            Element(scalar, vector, bivector, 'not an operator')


class TestElementProperties:

    def test_calculates_components_correctly(
        self, scalar, vector, bivector, fake_operator
    ):
        e = Element(scalar, vector, bivector, fake_operator)

        assert e.scalar == scalar
        assert e.vector == vector
        assert e.bivector == bivector

        assert e.x == approx(vector.x)
        assert e.y == approx(vector.y)
        assert e.xy == approx(bivector.xy)

        components = e.components
        assert isinstance(components, tuple)
        assert len(components) == 4
        assert components == (float(scalar), vector.x, vector.y, bivector.xy)

    def test_cannot_change_components(
        self, scalar, vector, bivector, fake_operator
    ):
        e = Element(scalar, vector, bivector, fake_operator)
        other_scalar = Scalar(ScalarData(2.4), fake_operator)
        other_vector = Vector(VectorData(2.4, 1), fake_operator)
        other_bivector = Bivector(BivectorData(2.4), fake_operator)

        with pytest.raises(AttributeError):
            e.scalar = other_scalar
        with pytest.raises(AttributeError):
            e.vector = other_vector
        with pytest.raises(AttributeError):
            e.bivector = other_bivector
        with pytest.raises(AttributeError):
            e.x = 4.1
        with pytest.raises(AttributeError):
            e.y = 4
        with pytest.raises(AttributeError):
            e.xy = 4.1
        with pytest.raises(AttributeError):
            e.components = (1, 3.4, 4.5, 1.3)

    def test_modulus_is_calculated_correctly(self):
        # TODO: Fazer quando eu souber calcular isso
        pass


class TestElementOperations:

    def test_element_equality(self, fake_operator):
        components = [
            (1.0, 2.0, 3.0, 4.0),
            (1.0, 2.0, 3.0, 4.0),
            (7.7, 2.0, 3.0, 4.0),
            (1.0, 7.7, 3.0, 4.0),
            (1.0, 2.0, 7.7, 4.0),
            (1.0, 2.0, 3.0, 7.7),
        ]

        elements = [
            Element(
                Scalar(ScalarData(comp[0]), fake_operator),
                Vector(VectorData(comp[1], comp[2]), fake_operator),
                Bivector(BivectorData(comp[3]), fake_operator),
                fake_operator
            )
            for comp in components
        ]

        assert elements[0] == elements[1]
        assert elements[0] != elements[2]
        assert elements[0] != elements[3]
        assert elements[0] != elements[4]
        assert elements[0] != elements[5]

    def test_negative_of_element(self, fake_operator):
        e = Element(
            Scalar(ScalarData(-1.2), fake_operator),
            Vector(VectorData(-0.4, 10), fake_operator),
            Bivector(BivectorData(-0.1), fake_operator),
            fake_operator
        )
        negative_e = Element(
            Scalar(ScalarData(1.2), fake_operator),
            Vector(VectorData(0.4, -10), fake_operator),
            Bivector(BivectorData(0.1), fake_operator),
            fake_operator
        )
        assert -e == negative_e

    def test_addition_calls_operator(self, element, fake_operator, mocker):
        mocker.patch.object(
            fake_operator, 'add', return_value='expected result')
        other = 'object to add'
        result = element + other
        fake_operator.add.assert_called_with(element, other)
        assert result == 'expected result'

    def test_right_addition_calls_operator(
        self, element, fake_operator, mocker
    ):
        mocker.patch.object(
            fake_operator, 'add', return_value='expected result')
        other = 'object to add'
        result = other + element
        fake_operator.add.assert_called_with(other, element)
        assert result == 'expected result'
