from typing import List

from sqlalchemy.orm import Session, Query
from database import engine
from user.models import UserModel

from .models import MeterType


class MeterTypeProvider:
    @staticmethod
    def create(**meter_type_fields):
        with Session(engine) as session:
            meter_type = MeterType(**meter_type_fields)
            session.add(meter_type)
            session.commit()

    @staticmethod
    def update(meter_type_id: int, **fields_to_update):
        with Session(engine) as session:
            session.query(MeterType).filter(MeterType.id == meter_type_id).update(fields_to_update)
            session.commit()

    @staticmethod
    def delete(meter_type_id: int):
        with Session(engine) as session:
            meter_type = session.query(MeterType).filter_by(id=meter_type_id).first()
            session.delete(meter_type)
            session.commit()

    @staticmethod
    def add_to_user_meter_types(user_id: int, meter_types_ids: List[int]):
        with Session(engine) as session:
            user = session.query(UserModel).filter_by(id=user_id).first()
            meter_types = session.query(MeterType).filter(MeterType.id.in_(meter_types_ids)).all()
            user.meter_types.extend(meter_types)
            session.add(user)
            session.commit()

    @staticmethod
    def delete_from_user_meter_types(user_id: int, meter_types_ids: List[int]):
        with Session(engine) as session:
            user = session.query(UserModel).filter_by(id=user_id).first()
            user_meter_types_set = set(user.meter_types)

            meter_types_set = set(session.query(MeterType).filter(MeterType.id.in_(meter_types_ids)).all())

            user.meter_types = list(user_meter_types_set.difference(meter_types_set))
            session.add(user)
            session.commit()

    @staticmethod
    def get_user_meter_types(user_id: int) -> Query:
        with Session(engine) as session:
            return session.query(MeterType).join(MeterType.users).filter(UserModel.id == user_id)
