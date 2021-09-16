import pytest
from pytest import approx

from representation.bivector import BivectorData
from domain.bivector import Bivector


class TestInitialization:

    def test_initialization_successful(self, fake_operator):
        bv_data = BivectorData(1.2)
        bv = Bivector(bv_data, fake_operator)
        assert bv._data == bv_data
        assert bv._operator == fake_operator

    def test_initialization_wrong_vector_data_type(self, fake_operator):
        with pytest.raises(TypeError):
            Bivector(4.3, fake_operator)

    def test_initialization_wrong_operator_type(self):
        with pytest.raises(TypeError):
            Bivector(BivectorData(1.2), 'not an operator')


class TestBivectorProperties:

    def test_calculates_components_correctly(self, fake_operator):
        bv = Bivector(BivectorData(1.5), fake_operator)
        components = bv.components
        assert isinstance(components, tuple)
        assert len(components) == 1
        assert components[0] == approx(1.5)

    def test_cannot_change_components(self, fake_operator):
        bv = Bivector(BivectorData(1.3), fake_operator)
        with pytest.raises(AttributeError):
            bv.xy = 4.1
        with pytest.raises(AttributeError):
            bv.components = (3.4, )

    @pytest.mark.parametrize('xy,expected_modulus', [
        (3, 3),
        (-4.2, 4.2),
        (0, 0)
    ])
    def test_modulus_is_calculated_correctly(
        self, xy, expected_modulus, fake_operator
    ):
        bv = Bivector(BivectorData(xy), fake_operator)
        assert bv.modulus == approx(expected_modulus)

    def test_direction_is_calculated_correctly(self, fake_operator):
        # TODO: Fazer quando eu souber calcular isso
        pass

    def test_direction_is_none_when_vector_is_null(self, fake_operator):
        # TODO: Fazer quando eu souber calcular isso
        pass


class TestBivectorOperations:

    def test_bivector_equality(self, fake_operator):
        bv1 = Bivector(BivectorData(1.2), fake_operator)
        bv2 = Bivector(BivectorData(1.2), fake_operator)
        bv3 = Bivector(BivectorData(1.1), fake_operator)
        assert bv1 == bv2
        assert bv1 != bv3

    def test_negative_of_bivector(self, fake_operator):
        bv = Bivector(BivectorData(1.2), fake_operator)
        negative_bv = Bivector(BivectorData(-1.2), fake_operator)
        assert -bv == negative_bv

    def test_addition_calls_operator(self, fake_operator, mocker):
        mocker.patch.object(
            fake_operator, 'add', return_value='expected result')
        bv = Bivector(BivectorData(2), fake_operator)
        other = 'object to add'
        result = bv + other
        fake_operator.add.assert_called_with(bv, other)
        assert result == 'expected result'

    def test_right_addition_calls_operator(self, fake_operator, mocker):
        mocker.patch.object(
            fake_operator, 'add', return_value='expected result')
        bv = Bivector(BivectorData(2), fake_operator)
        other = 'object to add'
        result = other + bv
        fake_operator.add.assert_called_with(other, bv)
        assert result == 'expected result'

    def test_abs_returns_modulus(self, fake_operator):
        bv = Bivector(BivectorData(-3.2), fake_operator)
        result_abs = abs(bv)
        assert abs(result_abs - bv.modulus) < 1e-6
