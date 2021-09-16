import pytest
from pytest import approx

from representation.bivector import BivectorData
from domain.bivector import Bivector


class TestInitialization:

    def test_initialization_successful(self, fake_adder):
        bv_data = BivectorData(1.2)
        bv = Bivector(bv_data, fake_adder)
        assert bv._data == bv_data
        assert bv._adder == fake_adder

    def test_initialization_wrong_vector_data_type(self, fake_adder):
        with pytest.raises(TypeError):
            Bivector(4.3, fake_adder)

    def test_initialization_wrong_adder_type(self):
        with pytest.raises(TypeError):
            Bivector(BivectorData(1.2), 'not an adder')


class TestBivectorProperties:

    def test_calculates_components_correctly(self, fake_adder):
        bv = Bivector(BivectorData(1.5), fake_adder)
        components = bv.components
        assert isinstance(components, tuple)
        assert len(components) == 1
        assert components[0] == approx(1.5)

    def test_cannot_change_components(self, fake_adder):
        bv = Bivector(BivectorData(1.3), fake_adder)
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
        self, xy, expected_modulus, fake_adder
    ):
        bv = Bivector(BivectorData(xy), fake_adder)
        assert bv.modulus == approx(expected_modulus)

    def test_direction_is_calculated_correctly(self, fake_adder):
        # TODO: Fazer quando eu souber calcular isso
        pass

    def test_direction_is_none_when_vector_is_null(self, fake_adder):
        # TODO: Fazer quando eu souber calcular isso
        pass


class TestBivectorOperations:

    def test_bivector_equality(self, fake_adder):
        bv1 = Bivector(BivectorData(1.2), fake_adder)
        bv2 = Bivector(BivectorData(1.2), fake_adder)
        bv3 = Bivector(BivectorData(1.1), fake_adder)
        assert bv1 == bv2
        assert bv1 != bv3

    def test_negative_of_bivector(self, fake_adder):
        bv = Bivector(BivectorData(1.2), fake_adder)
        negative_bv = Bivector(BivectorData(-1.2), fake_adder)
        assert -bv == negative_bv

    def test_addition_calls_adder(self, fake_adder, mocker):
        mocker.patch.object(fake_adder, 'add', return_value='expected result')
        bv = Bivector(BivectorData(2), fake_adder)
        other = 'object to add'
        result = bv + other
        fake_adder.add.assert_called_with(bv, other)
        assert result == 'expected result'

    def test_right_addition_calls_adder(self, fake_adder, mocker):
        mocker.patch.object(fake_adder, 'add', return_value='expected result')
        bv = Bivector(BivectorData(2), fake_adder)
        other = 'object to add'
        result = other + bv
        fake_adder.add.assert_called_with(other, bv)
        assert result == 'expected result'

    def test_abs_returns_modulus(self, fake_adder):
        bv = Bivector(BivectorData(-3.2), fake_adder)
        result_abs = abs(bv)
        assert abs(result_abs - bv.modulus) < 1e-6
