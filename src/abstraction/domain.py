from abc import ABC

from abstraction.representation import EntityData


class Entity(ABC):
    _data: EntityData
