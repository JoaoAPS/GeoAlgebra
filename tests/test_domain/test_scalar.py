import pytest
from pytest import approx
from domain.scalar import Scalar
from representation.scalar import ScalarData


class TestScalarInitialization:

    def test_initialization_successful(self, fake_operator):
        s = Scalar(ScalarData(1.2), fake_operator)
        assert s._data == ScalarData(1.2)
        assert s._operator == fake_operator

    def test_initialization_wrong_scalar_data_type(self, fake_operator):
        with pytest.raises(TypeError):
            Scalar(1.2, fake_operator)

    def test_initialization_wrong_operator_type(self):
        with pytest.raises(TypeError):
            Scalar(ScalarData(1.2), 'not an operator')


class TestScalarProperties:

    def test_propery_value(self, fake_operator):
        s = Scalar(ScalarData(1.5), fake_operator)
        assert s.value == approx(1.5)

    def test_scalar_is_immutable(self, fake_operator):
        s = Scalar(ScalarData(1), fake_operator)
        with pytest.raises(AttributeError):
            s.value = 2


class TestScalarOperations:

    def test_float_equivalence(self, fake_operator):
        s = Scalar(ScalarData(1.1), fake_operator)
        assert float(s) == approx(1.1)

    def test_equality_with_other_scalars(self, fake_operator):
        s1 = Scalar(ScalarData(2.0), fake_operator)
        s2 = Scalar(ScalarData(2.0), fake_operator)
        s3 = Scalar(ScalarData(2.5), fake_operator)
        assert s1 == s2
        assert s1 != s3

    def test_equality_with_numbers(self, fake_operator):
        s = Scalar(ScalarData(2.0), fake_operator)
        assert s == 2.0
        assert s != 3.1

    def test_negative_of_scalar(self, fake_operator):
        s = Scalar(ScalarData(2.0), fake_operator)
        negative_s = Scalar(ScalarData(-2.0), fake_operator)
        assert -s == negative_s

    def test_addition_calls_operator(self, fake_operator, mocker):
        mocker.patch.object(
            fake_operator, 'add', return_value='expected result')
        s1 = Scalar(ScalarData(2.0), fake_operator)
        other = 'object to add'
        result = s1 + other
        fake_operator.add.assert_called_with(s1, other)
        assert result == 'expected result'

    def test_right_addition_calls_operator(self, fake_operator, mocker):
        mocker.patch.object(
            fake_operator, 'add', return_value='expected result')
        s = Scalar(ScalarData(2.0), fake_operator)
        other = 'object to add'
        result = other + s
        fake_operator.add.assert_called_with(other, s)
        assert result == 'expected result'

    def test_abs_is_applied_as_float(self, fake_operator):
        s = Scalar(ScalarData(-1.0), fake_operator)
        assert abs(s) == approx(1.0)
