import pytest
from pytest import approx

from domain import Scalar, Vector


class TestScalarCreation:

    def test_creation_with_value(self, factory):
        s = factory.make_scalar(4.5)
        assert isinstance(s, Scalar)
        assert s.value == approx(4.5)

    def test_creation_deafult_value(self, factory):
        s = factory.make_scalar()
        assert isinstance(s, Scalar)
        assert s.value == approx(0)

    def test_creation_from_another_scalar(self, factory):
        s0 = factory.make_scalar(2.5)
        s = factory.make_scalar(s0)
        assert isinstance(s, Scalar)
        assert s.value == approx(2.5)

    @pytest.mark.parametrize('value', ['12', 'oi', [1], False])
    def test_creation_raises_error_if_value_is_not_number(
        self, value, factory
    ):
        with pytest.raises(TypeError):
            factory.make_scalar(value)


class TestVectorCreation:

    def test_creation_default_value(self, factory):
        v = factory.make_vector()
        assert isinstance(v, Vector)
        assert v.x == approx(0)
        assert v.y == approx(0)

    @pytest.mark.parametrize('x,y', [(3, 1), (0, 0), (-3.4, 1.5)])
    def test_creation_successful_passing_positional_components_separately(
        self, x, y, factory
    ):
        v = factory.make_vector(x, y)
        assert isinstance(v, Vector)
        assert v.x == approx(x)
        assert v.y == approx(y)

    @pytest.mark.parametrize('x,y', [
        ('3.4', 1.5), (1.4, 'oi'), ([4], 0), (0.4, True)])
    def test_creation_error_passing_positional_components_separately(
        self, x, y, factory
    ):
        with pytest.raises(TypeError):
            factory.make_vector(x, y)

    @pytest.mark.parametrize('x,y', [(3, 1), (0, 0), (-3.4, 1.5)])
    def test_creation_successful_passing_named_components_separately(
        self, x, y, factory
    ):
        v = factory.make_vector(x=x, y=y)
        assert isinstance(v, Vector)
        assert v.x == approx(x)
        assert v.y == approx(y)

    @pytest.mark.parametrize('x,y', [
        ('3.4', 1.5), (1.4, 'oi'), ([4], 0), (0.4, True)])
    def test_creation_error_passing_named_components_separately(
        self, x, y, factory
    ):
        with pytest.raises(TypeError):
            factory.make_vector(x=x, y=y)

    @pytest.mark.parametrize('x,y', [(1, 5), (0, 0), (-3.4, 1.5)])
    def test_creation_successful_passing_positional_tuple(self, x, y, factory):
        v = factory.make_vector((x, y))
        assert isinstance(v, Vector)
        assert v.x == approx(x)
        assert v.y == approx(y)

    @pytest.mark.parametrize('x,y', [('3.4', 1.5), (1.4, 'oi'), ([4], 0)])
    def test_creation_errors_passing_positional_tuple(self, x, y, factory):
        with pytest.raises(TypeError):
            factory.make_vector((x, y))

    @pytest.mark.parametrize('x,y', [(1, 5), (0, 0), (-3.4, 1.5)])
    def test_creation_successful_passing_named_tuple(self, x, y, factory):
        v = factory.make_vector(components=(x, y))
        assert isinstance(v, Vector)
        assert v.x == approx(x)
        assert v.y == approx(y)

    @pytest.mark.parametrize('x,y', [('3.4', 1.5), (1.4, 'oi'), ([4], 0)])
    def test_creation_errors_passing_named_tuple(self, x, y, factory):
        with pytest.raises(TypeError):
            factory.make_vector(components=(x, y))

    def test_named_argument_takes_precedence_over_positional(self, factory):
        v1 = factory.make_vector(-1.0, -2.0, components=(3.0, 4.0))
        assert v1.x == approx(3)
        assert v1.y == approx(4)

        v2 = factory.make_vector((-1.0, -2.0), components=(3.0, 4.0))
        assert v2.x == approx(3)
        assert v2.y == approx(4)

        v3 = factory.make_vector(-1.0, -2.0, x=3.0, y=4.0)
        assert v3.x == approx(3)
        assert v3.y == approx(4)

        v4 = factory.make_vector((-1.0, -2.0), x=3.0, y=4.0)
        assert v4.x == approx(3)
        assert v4.y == approx(4)

    def test_sepate_components_take_precedence_over_tuple(self, factory):
        v = factory.make_vector(components=(-1.0, -2.0), x=3.0, y=4.0)
        assert v.x == approx(3)
        assert v.y == approx(4)

    def test_defining_only_one_of_the_components(self, factory):
        v1 = factory.make_vector(x=2.0)
        assert v1.x == approx(2)
        assert v1.y == approx(0)

        v2 = factory.make_vector(y=2.0)
        assert v2.x == approx(0)
        assert v2.y == approx(2)
