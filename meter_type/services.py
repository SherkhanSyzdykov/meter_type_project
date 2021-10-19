from sqlalchemy.orm import Query

from .models import MeterType
from .provider import MeterTypeProvider


class UserMeterTypesQuery:
    @classmethod
    def get_base_query(cls, user_id: int) -> Query:
        return MeterTypeProvider.get_user_meter_types(user_id)

    @classmethod
    def created_acs(cls, user_id: int) -> Query:
        return cls.get_base_query(user_id).order_by(MeterType.created_at)

    @classmethod
    def created_desc(cls, user_id: int) -> Query:
        return cls.get_base_query(user_id).order_by(MeterType.created_at.desc())
