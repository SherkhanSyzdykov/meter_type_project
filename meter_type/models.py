from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime
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

    created_at = Column(DateTime, default=datetime.now())

    users = relationship('UserModel', secondary='user_meter_type_association', back_populates='meter_types')

    def __repr__(self):
        return f'{self.id}: meter_type'
