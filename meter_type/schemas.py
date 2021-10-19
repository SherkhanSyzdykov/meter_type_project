from typing import List, Optional
from pydantic import BaseModel


class MeterTypeBaseModel(BaseModel):
    name: str
    coefficient: Optional[float] = None
    unit_of_measure: Optional[str] = None
    init_indicator_multiplier: Optional[float] = None
    description: Optional[float] = None

    class Config:
        orm_mode = True
