import pytest
from pytest import approx

from representation.vector import VectorData
from domain.vector import Vector


class TestVectorInitialization:

    def test_initialization_successful(self, fake_operator):
        v_data = VectorData(1.2, -0.2)
        v = Vector(v_data, fake_operator)
        assert v._data == v_data
        assert v._operator == fake_operator

    def test_initialization_wrong_vector_data_type(self, fake_operator):
        with pytest.raises(TypeError):
            Vector((1, 4.3), fake_operator)

    def test_initialization_wrong_operator_type(self):
        with pytest.raises(TypeError):
            Vector(VectorData(1.2, 1), 'not an operator')


class TestVectorProperties:

    def test_calculates_components_correctly(self, fake_operator):
        v = Vector(VectorData(3.4, 1.5), fake_operator)
        components = v.components

        assert v.x == approx(3.4)
        assert v.y == approx(1.5)
        assert isinstance(components, tuple)
        assert len(components) == 2
        assert components[0] == approx(3.4)
        assert components[1] == approx(1.5)

    def test_cannot_change_components(self, fake_operator):
        v = Vector(VectorData(1, 3), fake_operator)
        with pytest.raises(AttributeError):
            v.x = 4.1
        with pytest.raises(AttributeError):
            v.y = 4
        with pytest.raises(AttributeError):
            v.components = (1, 3.4)

    @pytest.mark.parametrize('components,expected_modulus', [
        ((3, 4), 5),
        ((3, -4), 5),
        ((1.5, -2.5), 2.915475),
        ((4.2, 0), 4.2),
        ((0, 0), 0),
    ])
    def test_modulus_is_calculated_correctly(
        self, components, expected_modulus, fake_operator
    ):
        v = Vector(VectorData(*components), fake_operator)
        assert v.modulus == approx(expected_modulus)

    def test_direction_is_calculated_correctly(self, fake_operator):
        # TODO: Fazer quando eu souber calcular isso
        pass

    def test_direction_is_none_when_vector_is_null(self, fake_operator):
        # TODO: Fazer quando eu souber calcular isso
        pass


class TestVectorOperations:

    def test_vector_equality(self, fake_operator):
        v1 = Vector(VectorData(1.2, 3), fake_operator)
        v2 = Vector(VectorData(1.2, 3), fake_operator)
        v3 = Vector(VectorData(1.1, 3), fake_operator)
        assert v1 == v2
        assert v1 != v3

    def test_negative_of_vector(self, fake_operator):
        v = Vector(VectorData(2.0, -1.5), fake_operator)
        negative_v = Vector(VectorData(-2.0, 1.5), fake_operator)
        assert -v == negative_v

    def test_addition_calls_operator(self, fake_operator, mocker):
        mocker.patch.object(
            fake_operator, 'add', return_value='expected result')
        v = Vector(VectorData(2, 1), fake_operator)
        other = 'object to add'
        result = v + other
        fake_operator.add.assert_called_with(v, other)
        assert result == 'expected result'

    def test_right_addition_calls_operator(self, fake_operator, mocker):
        mocker.patch.object(
            fake_operator, 'add', return_value='expected result')
        v = Vector(VectorData(2, 0), fake_operator)
        other = 'object to add'
        result = other + v
        fake_operator.add.assert_called_with(other, v)
        assert result == 'expected result'

    def test_abs_returns_modulus(self, fake_operator):
        v = Vector(VectorData(2.1, -3.2), fake_operator)
        result_abs = abs(v)
        assert abs(result_abs - v.modulus) < 1e-6
