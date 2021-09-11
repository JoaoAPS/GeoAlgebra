import dataclasses

from abstraction.representation import EntityData
from .scalar import ScalarData
from .vector import VectorData
from .bivector import BivectorData


@dataclasses.dataclass(frozen=True)
class ElementData(EntityData):
    scalar: ScalarData = ScalarData()
    vector: VectorData = VectorData()
    bivector: BivectorData = BivectorData()
