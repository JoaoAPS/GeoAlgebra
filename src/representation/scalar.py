import dataclasses

from abstraction.representation import EntityData


@dataclasses.dataclass(order=True, frozen=True)
class ScalarData(EntityData):
    value: float = 0.0
