from typing import List, Optional

from sqlalchemy.orm import Query, joinedload
from sqlalchemy.sql import select
from database import session
from user.models import UserModel

from .models import MeterType
from .schemas import MeterTypesList, MeterTypeRead


class MeterTypeSelector:
    FIELDS_TO_FILTER = {
        'coefficient__gt': MeterType.coefficient.__gt__,
        'unit_of_measure': MeterType.unit_of_measure.__eq__,
        'users__first_name': UserModel.first_name.__eq__,
    }

    @staticmethod
    def base_query(**kwargs) -> Query:
        return Query(MeterType, session=session).join(MeterType.users)

    @staticmethod
    def filter(query: Query, **kwargs) -> Query:
        for key, value in kwargs.items():
            if column_operator := MeterTypeSelector.FIELDS_TO_FILTER.get(key, None):
                q = column_operator(value)
                query = query.filter(q)
        return query


class MeterTypeProvider:
    @staticmethod
    def get_many_with_filter(**attrs_for_filter) -> MeterTypesList:
        base_query = MeterTypeSelector.base_query()
        query = MeterTypeSelector.filter(base_query, **attrs_for_filter)
        print(query)
        orm_meter_types = query.all()
        print()
        return MeterTypesList.from_orm(orm_meter_types)

    @staticmethod
    def get_one_with_filter(**attrs_for_filter) -> MeterTypeRead:
        orm_meter_type = session.query(MeterType).filter_by(**attrs_for_filter).first()
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
