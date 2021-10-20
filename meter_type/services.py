from sqlalchemy.orm import Query
from user.models import UserModel

from .models import MeterType
from .provider import MeterTypeProvider


class MeterTypeQuery:
    @staticmethod
    def get() -> Query:
        return MeterTypeProvider.get_query()

    @staticmethod
    def user_meter_types(user_id: int) -> Query:
        return MeterTypeProvider.get_query().join(MeterType.users).filter(UserModel.id == user_id)

    @staticmethod
    def ordered_by_created_at_field(*, desc=False) -> Query:
        attr_for_order = MeterType.created_at if not desc else MeterType.created_at.desc()
        return MeterTypeProvider.get_query().order_by(attr_for_order)


