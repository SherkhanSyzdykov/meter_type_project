from sqlalchemy import Column, Integer, String, Float
from database import Base


class MeterType(Base):
    __tablename__ = 'meter_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    coefficient = Column(Float)
    unit_of_measure = Column(String)
    init_indicator_multiplier = Column(Float)
    description = Column(String)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for kwarg in kwargs:
            setattr(self, kwarg, kwargs[kwarg])
