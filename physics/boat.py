"""
Concatenation of all singular models into a global boat model.
"""

from dataclasses import dataclass
from geometry.boat import Boat
from physics.context import Context

from typing import Any, Optional, Protocol


@dataclass
class Result:
    """Result of a call to a boat model
    to allow for error as value kind of implementation"""

    ok: bool
    msg: Optional[str] = None
    result: dict[str, Any] = {}


class BoatModel(Protocol):
    """Calculates equilibrium state of a boat geometry in given sailing conditions and geometric position"""

    def calculate(
        self,
        TWA: float,
        TWS: float,
        vb: float,
        phi: float,
        leeway_speed: float,
        **kwargs: Any,
    ) -> Result:
        """kwargs are used to pass trim, sail choice, etc."""
        ...

    def parameters(self) -> dict[str, Any]:
        pass


def generate_boat_model(
    boat: Boat,
    context: Context,
    parameter: dict[str, Any],
) -> BoatModel:
    pass
