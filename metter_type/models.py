from sqlalchemy import Column, Integer, String, Float
from database import Base


class MetterType(Base):
    __tablename__ = 'metter_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    coefficient = Column(Float)
    unit_of_measure = Column(String)
    init_indicator_multiplier = Column(Float)
    description = Column(String)
