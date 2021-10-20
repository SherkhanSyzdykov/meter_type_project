from typing import List

from sqlalchemy.orm import Query
from database import session
from user.models import UserModel

from .models import MeterType


class MeterTypeProvider:
    @staticmethod
    def get_query() -> Query:
        return session.query(MeterType)

    @staticmethod
    def create(**meter_type_fields):
        meter_type = MeterType(**meter_type_fields)
        session.add(meter_type)
        session.commit()

    @staticmethod
    def update(meter_type_id: int, **fields_to_update):
        session.query(MeterType).filter(MeterType.id == meter_type_id).update(fields_to_update)
        session.commit()

    @staticmethod
    def delete(meter_type_id: int):
        meter_type = session.query(MeterType).filter_by(id=meter_type_id).first()
        session.delete(meter_type)
        session.commit()

    @staticmethod
    def add_to_user_meter_types(user_id: int, meter_types_ids: List[int]):
        user = session.query(UserModel).filter_by(id=user_id).first()
        meter_types = session.query(MeterType).filter(MeterType.id.in_(meter_types_ids)).all()
        user.meter_types.extend(meter_types)
        session.add(user)
        session.commit()

    @staticmethod
    def delete_from_user_meter_types(user_id: int, meter_types_ids: List[int]):
        user = session.query(UserModel).filter_by(id=user_id).first()
        user_meter_types_set = set(user.meter_types)

        meter_types_set = set(session.query(MeterType).filter(MeterType.id.in_(meter_types_ids)).all())

        user.meter_types = list(user_meter_types_set.difference(meter_types_set))
        session.add(user)
        session.commit()
