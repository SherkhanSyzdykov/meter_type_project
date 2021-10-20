from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class MeterTypeBaseModel(BaseModel):
    name: str
    coefficient: Optional[float] = None
    unit_of_measure: Optional[str] = None
    init_indicator_multiplier: Optional[float] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class MeterTypeRead(MeterTypeBaseModel):
    id: int
    created_at: Optional[datetime] = None


class MeterTypeCreate(MeterTypeBaseModel):
    ...


class MeterTypesList(BaseModel):
    __root__: List[MeterTypeRead]

    class Config:
        orm_mode = True
