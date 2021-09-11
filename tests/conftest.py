# Adiciona src ao path
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))


from pytest import fixture
from abstraction.operations import AbstractAdd


class FakeAdd(AbstractAdd):

    def add(self, entity1, entity2):
        return (entity1, entity2)


@fixture
def fake_adder():
    return FakeAdd()
