import pytest
from pytest import approx

from representation import ScalarData, VectorData, BivectorData
from domain import Scalar, Vector, Bivector, Element


class TestScalarCreation:

    def test_creation_with_value(self, factory):
        s = factory.make_scalar(4.5)
        assert isinstance(s, Scalar)
        assert s.value == approx(4.5)

    def test_creation_deafult_value(self, factory):
        s = factory.make_scalar()
        assert isinstance(s, Scalar)
        assert s.value == approx(0)

    def test_creation_from_scalar_data(self, factory):
        s_data = ScalarData(5.4)
        s = factory.make_scalar(s_data)
        assert isinstance(s, Scalar)
        assert s.value == approx(5.4)

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


class TestVectorCreationPassingPositionalArguments:

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

    def test_creation_from_vector_data(self, factory):
        v_data = VectorData(5.4, 0.5)
        v = factory.make_vector(v_data)
        assert isinstance(v, Vector)
        assert v.x == approx(5.4)
        assert v.y == approx(0.5)

    def test_creation_from_other_vector(self, factory):
        v0 = factory.make_vector(4.2, 5.1)
        v = factory.make_vector(v0)
        assert isinstance(v, Vector)
        assert v == v0


class TestVectorCreationPassingNamedArguments:

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


class TestBivectorCreation:

    def test_creation_default_value(self, factory):
        bv = factory.make_bivector()
        assert isinstance(bv, Bivector)
        assert bv.xy == approx(0)

    @pytest.mark.parametrize('xy', [3, 0, -3.4, 1.5])
    def test_creation_successful(self, xy, factory):
        bv = factory.make_bivector(xy)
        assert isinstance(bv, Bivector)
        assert bv.xy == approx(xy)

    @pytest.mark.parametrize('xy', ['3.4', 'oi', [4], False])
    def test_creation_errors(self, xy, factory):
        with pytest.raises(TypeError):
            factory.make_bivector(xy)

    def test_creation_from_bivector_data(self, factory):
        bv_data = BivectorData(5.4)
        bv = factory.make_bivector(bv_data)
        assert isinstance(bv, Bivector)
        assert bv.xy == approx(5.4)

    def test_creation_from_other_bivector(self, factory):
        bv0 = factory.make_bivector(3.3)
        bv = factory.make_bivector(bv0)
        assert isinstance(bv, Bivector)
        assert bv == bv0


class TestElementCreationPassingPositionalArguments:

    def test_creation_passing_positional_entities(
        self, factory, scalar, vector, bivector
    ):
        e = factory.make_element(scalar, vector, bivector)
        assert isinstance(e, Element)
        assert e.scalar == scalar
        assert e.vector == vector
        assert e.bivector == bivector

    def test_creation_error_passing_positional_entities(
        self, scalar, vector, bivector, factory
    ):
        with pytest.raises(TypeError):
            factory.make_element(bivector, vector, bivector)
        with pytest.raises(TypeError):
            factory.make_element(scalar, scalar, bivector)
        with pytest.raises(TypeError):
            factory.make_element(scalar, vector, vector)

    def test_creation_passing_positional_individual_components(self, factory):
        e = factory.make_element(1.0, 2.0, 3.0, 4.0)
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar(1.0)
        assert e.vector == factory.make_vector(2.0, 3.0)
        assert e.bivector == factory.make_bivector(4.0)

    @pytest.mark.parametrize('s,x,y,xy', [
        ('3.4', 1.5, 0.4, 0.4),
        (1.4, 'oi', 1.0, 1.0),
        (1.0, 1.0, [4], 0),
        (1.0, 1.0, 0.4, True)
    ])
    def test_creation_error_passing_positional_individual_components(
        self, s, x, y, xy, factory
    ):
        with pytest.raises(TypeError):
            factory.make_element(s, x, y, xy)

    def test_creation_passing_positional_tuple_components(self, factory):
        e = factory.make_element((1.0, 2.0, 3.0, 4.0))
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar(1.0)
        assert e.vector == factory.make_vector(2.0, 3.0)
        assert e.bivector == factory.make_bivector(4.0)

    @pytest.mark.parametrize('s,x,y,xy', [
        ('3.4', 1.5, 0.4, 0.4),
        (1.4, 'oi', 1.0, 1.0),
        (1.0, 1.0, [4], 0),
        (1.0, 1.0, 0.4, True)
    ])
    def test_creation_error_passing_positional_tuple_components(
        self, s, x, y, xy, factory
    ):
        with pytest.raises(TypeError):
            factory.make_element((s, x, y, xy))

    def test_creation_error_passing_incomplete_positional_tuple_components(
        self, factory
    ):
        with pytest.raises(ValueError):
            factory.make_element((1.0, 2.0, 3.0))

    def test_creation_all_default_values(self, factory):
        e = factory.make_element()
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar()
        assert e.vector == factory.make_vector()
        assert e.bivector == factory.make_bivector()

    def test_creation_vector_and_bivector_default_value_positional(
        self, factory
    ):
        e = factory.make_element(1.0)
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar(1.0)
        assert e.vector == factory.make_vector()
        assert e.bivector == factory.make_bivector()

    def test_creation_vector_y_default_value_positional(self, factory):
        e = factory.make_element(1.0, 2.0)
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar(1.0)
        assert e.vector == factory.make_vector(2.0)
        assert e.bivector == factory.make_bivector()

    def test_creation_bivector_default_value_positional(self, factory):
        e = factory.make_element(1.0, 2.0, 3.0)
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar(1.0)
        assert e.vector == factory.make_vector(2.0, 3.0)
        assert e.bivector == factory.make_bivector()

    def test_creation_from_other_element(self, factory):
        e0 = factory.make_element(1.2, 7.0, 4.2, 5.1)
        e = factory.make_element(e0)
        assert isinstance(e, Element)
        assert e == e0


class TestElementCreationPassingNamedArguments:

    def test_creation_passing_named_entities(
        self, factory, scalar, vector, bivector
    ):
        e = factory.make_element(
            scalar=scalar, vector=vector, bivector=bivector)
        assert isinstance(e, Element)
        assert e.scalar == scalar
        assert e.vector == vector
        assert e.bivector == bivector

    def test_creation_error_passing_named_entities(
        self, scalar, vector, bivector, factory
    ):
        with pytest.raises(TypeError):
            factory.make_element(
                scalar=bivector, vector=vector, bivector=bivector)
        with pytest.raises(TypeError):
            factory.make_element(
                scalar=scalar, vector=scalar, bivector=bivector)
        with pytest.raises(TypeError):
            factory.make_element(
                scalar=scalar, vector=vector, bivector=vector)

    def test_creation_passing_named_individual_components(self, factory):
        e = factory.make_element(scalar=1.0, x=2.0, y=3.0, xy=4.0)
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar(1.0)
        assert e.vector == factory.make_vector(2.0, 3.0)
        assert e.bivector == factory.make_bivector(4.0)

    @pytest.mark.parametrize('s,x,y,xy', [
        ('3.4', 1.5, 0.4, 0.4),
        (1.4, 'oi', 1.0, 1.0),
        (1.0, 1.0, [4], 0),
        (1.0, 1.0, 0.4, True)
    ])
    def test_creation_error_passing_named_individual_components(
        self, s, x, y, xy, factory
    ):
        with pytest.raises(TypeError):
            factory.make_element(scalar=s, x=x, y=y, xy=xy)

    def test_creation_passing_named_tuple_components(self, factory):
        e = factory.make_element(components=(1.0, 2.0, 3.0, 4.0))
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar(1.0)
        assert e.vector == factory.make_vector(2.0, 3.0)
        assert e.bivector == factory.make_bivector(4.0)

    @pytest.mark.parametrize('s,x,y,xy', [
        ('3.4', 1.5, 0.4, 0.4),
        (1.4, 'oi', 1.0, 1.0),
        (1.0, 1.0, [4], 0),
        (1.0, 1.0, 0.4, True)
    ])
    def test_creation_error_passing_named_tuple_components(
        self, s, x, y, xy, factory
    ):
        with pytest.raises(TypeError):
            factory.make_element(components=(s, x, y, xy))

    def test_creation_error_passing_incomplete_named_tuple_components(
        self, factory
    ):
        with pytest.raises(ValueError):
            factory.make_element(components=(1.0, 2.0, 3.0))

    def test_creation_passing_only_named_scalar(
        self, factory
    ):
        e = factory.make_element(scalar=1.0)
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar(1.0)
        assert e.vector == factory.make_vector()
        assert e.bivector == factory.make_bivector()

    def test_creation_passing_only_named_vector(self, factory):
        v = factory.make_vector(1.0, 2.0)
        e = factory.make_element(vector=v)
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar()
        assert e.vector == v
        assert e.bivector == factory.make_bivector()

    def test_creation_passing_only_named_bivector(self, factory):
        bv = factory.make_bivector(1.0)
        e = factory.make_element(bivector=bv)
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar()
        assert e.vector == factory.make_vector()
        assert e.bivector == bv

    def test_creation_passing_only_named_x(self, factory):
        e = factory.make_element(x=5.0)
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar()
        assert e.vector == factory.make_vector(x=5.0)
        assert e.bivector == factory.make_bivector()

    def test_creation_passing_only_named_y(self, factory):
        e = factory.make_element(y=5.0)
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar()
        assert e.vector == factory.make_vector(y=5.0)
        assert e.bivector == factory.make_bivector()

    def test_creation_passing_only_named_xy(self, factory):
        e = factory.make_element(xy=5.0)
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar()
        assert e.vector == factory.make_vector()
        assert e.bivector == factory.make_bivector(5.0)

    def test_entities_take_precedence_over_indivudual_components(
        self, factory, scalar, vector, bivector
    ):
        e = factory.make_element(
            scalar=scalar,
            vector=vector,
            bivector=bivector,
            x=-7.0,
            y=77.0,
            xy=15.0
        )
        assert isinstance(e, Element)
        assert e.scalar == scalar
        assert e.vector == vector
        assert e.bivector == bivector

    def test_indivudual_components_take_precedence_over_tuple_components(
        self, factory
    ):
        e = factory.make_element(
            scalar=1.0,
            x=2.0,
            y=3.0,
            xy=4.0,
            components=(-10, -11, -12, -13)
        )
        assert isinstance(e, Element)
        assert e.scalar == factory.make_scalar(1.0)
        assert e.vector == factory.make_vector(2.0, 3.0)
        assert e.bivector == factory.make_bivector(4.0)
