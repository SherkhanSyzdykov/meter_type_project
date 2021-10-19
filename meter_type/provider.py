from typing import List

from sqlalchemy.orm import Session
from database import engine
from user.models import UserModel, user_meter_type_association_table

from .models import MeterType


class MeterTypeProvider:
    def create(self, **meter_type_fields):
        with Session(engine) as session:
            meter_type = MeterType(**meter_type_fields)
            session.add(meter_type)
            session.commit()

    def update(self, meter_type_id: int, **fields_to_update):
        with Session(engine) as session:
            session.query(MeterType).filter(MeterType.id == meter_type_id).update(fields_to_update)
            session.commit()

    def delete(self, meter_type_id: int):
        with Session(engine) as session:
            meter_type = session.query(MeterType).filter_by(id=meter_type_id).first()
            session.delete(meter_type)
            session.commit()

    def add_to_user_meter_types(self, user_id: int, meter_types_ids: List[int]):
        with Session(engine) as session:
            user = session.query(UserModel).filter_by(id=user_id).first()
            meter_types = session.query(MeterType).filter(MeterType.id.in_(meter_types_ids)).all()
            user.meter_types.extend(meter_types)
            session.add(user)
            session.commit()

    def delete_from_user_meter_types(self, user_id: int, meter_types_ids: List[int]):
        with Session(engine) as session:
            user = session.query(UserModel).filter_by(id=user_id).first()
            user_meter_types_set = set(user.meter_types)

            meter_types_set = set(session.query(MeterType).filter(MeterType.id.in_(meter_types_ids)).all())

            user.meter_types = list(user_meter_types_set.difference(meter_types_set))
            session.add(user)
            session.commit()

    def get_user_meter_types(self, user_id: int) -> list:
        with Session(engine) as session:
            return session.query(MeterType).join(MeterType.users).filter(UserModel.id == user_id).all()

