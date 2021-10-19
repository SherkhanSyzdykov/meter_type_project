from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base


class MeterType(Base):
    __tablename__ = 'meter_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    coefficient = Column(Float)
    unit_of_measure = Column(String)
    init_indicator_multiplier = Column(Float)
    description = Column(String)

    users = relationship('UserModel', secondary='user_meter_type_association', back_populates='meter_types')
