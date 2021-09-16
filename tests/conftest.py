# Adiciona src ao path
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))


from pytest import fixture

from abstraction.operations import (
    Operator,
    AbstractAdder,
    AbstractSubtractor,
    AbstractInnerProduct,
    AbstractOuterProduct
)


# ----- Fake Operations ---
class FakeAdder(AbstractAdder):

    def add(self, entity1, entity2):
        return ('add', entity1, entity2)


class FakeSubtractor(AbstractSubtractor):

    def subtract(self, entity1, entity2):
        return ('subtract', entity1, entity2)


class FakeInnerProduct(AbstractInnerProduct):

    def inner(self, entity1, entity2):
        return ('inner', entity1, entity2)


class FakeOuterProduct(AbstractOuterProduct):

    def outer(self, entity1, entity2):
        return ('outer', entity1, entity2)


@fixture
def fake_operator():
    return Operator(
        adder=FakeAdder(),
        subtractor=FakeSubtractor(),
        inner_product=FakeInnerProduct(),
        outer_product=FakeOuterProduct()
    )
