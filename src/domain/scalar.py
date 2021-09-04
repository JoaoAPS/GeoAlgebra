from typing import Optional
from .abstract import AbstractScalar

class Scalar(AbstractScalar, float):

    def __init__(self, value: Optional[float] = None):
        if value is None:
            value = 0.0
        self._value = float(value)
        super().__init__()

    @property
    def value(self) -> float:
        return self._value
