import pytest
from pytest import approx
from domain.scalar import Scalar
from representation.scalar import ScalarData


def test_initialization_successful(fake_adder):
    s = Scalar(ScalarData(1.2), fake_adder)
    assert s._data == ScalarData(1.2)
    assert s._adder == fake_adder


def test_initialization_wrong_scalar_data_type(fake_adder):
    with pytest.raises(TypeError):
        Scalar(1.2, fake_adder)


def test_initialization_wrong_adder_type():
    with pytest.raises(TypeError):
        Scalar(ScalarData(1.2), 'not an adder')


def test_propery_value(fake_adder):
    s = Scalar(ScalarData(1.5), fake_adder)
    assert s.value == approx(1.5)


def test_float_equivalence(fake_adder):
    s = Scalar(ScalarData(1.1), fake_adder)
    assert float(s) == approx(1.1)


def test_scalar_is_immutable(fake_adder):
    s = Scalar(ScalarData(1), fake_adder)
    with pytest.raises(AttributeError):
        s.value = 2


def test_equality_with_other_scalars(fake_adder):
    s1 = Scalar(ScalarData(2.0), fake_adder)
    s2 = Scalar(ScalarData(2.0), fake_adder)
    s3 = Scalar(ScalarData(2.5), fake_adder)
    assert s1 == s2
    assert s1 != s3


def test_equality_with_numbers(fake_adder):
    s1 = Scalar(ScalarData(2.0), fake_adder)
    assert s1 == 2.0
    assert s1 != 3.1


def test_addition_calls_adder(fake_adder, mocker):
    mocker.patch.object(fake_adder, 'add', return_value='expected result')
    s1 = Scalar(ScalarData(2.0), fake_adder)
    other = 'object to add'
    result = s1 + other
    fake_adder.add.assert_called_with(s1, other)
    assert result == 'expected result'


def test_right_addition_calls_adder(fake_adder, mocker):
    mocker.patch.object(fake_adder, 'add', return_value='expected result')
    s1 = Scalar(ScalarData(2.0), fake_adder)
    other = 'object to add'
    result = other + s1
    fake_adder.add.assert_called_with(other, s1)
    assert result == 'expected result'


def test_abs_is_applied_as_float(fake_adder):
    s = Scalar(ScalarData(-1.0), fake_adder)
    assert abs(s) == approx(1.0)
