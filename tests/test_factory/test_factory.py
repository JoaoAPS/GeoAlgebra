from domain.scalar import Scalar
from domain.vector import Vector
from domain.bivector import Bivector
from domain.element import Element


class TestScalarCreation:

    def test_returns_a_scalar(self, factory):
        s = factory.scalar(1.2)
        assert isinstance(s, Scalar)

    def test_calls_scalar_init_method_with_passed_arguments(
        self, factory, mocker
    ):
        mock_scalar_init = mocker.patch(
            'domain.scalar.Scalar.__init__', return_value=None)
        factory.scalar(1.2)
        mock_scalar_init.assert_called_with(1.2)


class TestVectorCreation:

    def test_returns_a_vector(self, factory):
        s = factory.vector(1.2, 6.1)
        assert isinstance(s, Vector)

    def test_calls_vector_init_method_with_passed_arguments(
        self, factory, mocker
    ):
        mock_vector_init = mocker.patch(
            'domain.vector.Vector.__init__', return_value=None)
        factory.vector('input')
        mock_vector_init.assert_called_with('input')


class TestBivectorCreation:

    def test_returns_a_bivector(self, factory):
        s = factory.bivector(1.2)
        assert isinstance(s, Bivector)

    def test_calls_bivector_init_method_with_passed_arguments(
        self, factory, mocker
    ):
        mock_bivector_init = mocker.patch(
            'domain.bivector.Bivector.__init__', return_value=None)
        factory.bivector('input')
        mock_bivector_init.assert_called_with('input')


class TestElementCreation:

    def test_returns_an_element(self, factory):
        s = factory.element(1.2, 6.1, 0.4)
        assert isinstance(s, Element)

    def test_calls_element_init_method_with_passed_arguments(
        self, factory, mocker
    ):
        mock_element_init = mocker.patch(
            'domain.element.Element.__init__', return_value=None)
        factory.element('input')
        mock_element_init.assert_called_with('input')
