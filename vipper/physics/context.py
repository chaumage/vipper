"""
    Context of the boat: wind, sea, heading, etc.
"""

from pydantic import BaseModel

class Context(BaseModel):
    """Parameters that are set by the engineer before calculation"""
    TWA: float # True Wind Angle
    TWS: float # True Wind Speed
    
