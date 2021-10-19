from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from meter_type.models import MeterType

user_meter_type_association_table = Table('user_meter_type_association', Base.metadata,
                          Column('user_id', ForeignKey('user_model.id'), primary_key=True),
                          Column('meter_type_id', ForeignKey('meter_type.id'), primary_key=True))


class UserModel(Base):
    __tablename__ = 'user_model'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))

    meter_types = relationship(MeterType, secondary=user_meter_type_association_table, back_populates='users')

