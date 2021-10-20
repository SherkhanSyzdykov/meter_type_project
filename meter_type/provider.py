from typing import List, Optional

from database import session
from user.models import UserModel

from .models import MeterType
from .schemas import MeterTypesList, MeterTypeRead


class MeterTypeProvider:
    @staticmethod
    def get_by_id(id: int) -> MeterTypeRead:
        orm_meter_type = session.query(MeterType).filter(MeterType.id == id).first()
        return MeterTypeRead.from_orm(orm_meter_type)

    @staticmethod
    def get_all() -> MeterTypesList:
        orm_meter_types = session.query(MeterType).all()
        return MeterTypesList.from_orm(orm_meter_types)

    @staticmethod
    def get_user_meter_types(user_id: int) -> MeterTypesList:
        orm_meter_types = session.query(MeterType).join(MeterType.users).filter(UserModel.id == user_id).all()
        return MeterTypesList.from_orm(orm_meter_types)

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
