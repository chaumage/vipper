"""
Hull geometries.
"""

from pydantic import BaseModel


class SimpleHull(BaseModel):
    name: str
    WSA: float  # Wetted Surface Area
    Lwl: float  # waterline length
    Vol: float  # volume of canoe body
    Bwl: float  # waterline beam
    Tc: float  # Canoe body draft
    Tmax: float  # Maximum draft of yacht
    Amax: float  # Max section area
    Boa: float  #
    ff: float  #
    fa: float  #
