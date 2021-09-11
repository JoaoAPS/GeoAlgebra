import dataclasses

from abstraction.representation import EntityData


@dataclasses.dataclass(frozen=True)
class BivectorData(EntityData):
    xy: float = 0.0
