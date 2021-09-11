import dataclasses

from abstraction.representation import EntityData


@dataclasses.dataclass(frozen=True)
class VectorData(EntityData):
    x: float = 0.0
    y: float = 0.0
