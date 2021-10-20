from typing import List

from .provider import MeterTypeProvider
from .schemas import MeterTypesList, MeterTypeCreate, MeterTypeRead


class MeterTypeService:
    @staticmethod
    def get_meter_types() -> MeterTypesList:
        return MeterTypeProvider.get_all()

    @staticmethod
    def get_meter_type(meter_type_id: int) -> MeterTypeRead:
        return MeterTypeProvider.get_by_id(meter_type_id)

    @staticmethod
    def get_user_meter_types(user_id: int) -> MeterTypesList:
        return MeterTypeProvider.get_user_meter_types(user_id)

    @staticmethod
    def create_meter_type(meter_type: MeterTypeCreate):
        MeterTypeProvider.create(**meter_type.dict())

    @staticmethod
    def add_to_user_meter_types(user_id: int, meter_types_ids: List[int]):
        MeterTypeProvider.add_to_user_meter_types(user_id, meter_types_ids)

    @staticmethod
    def delete_from_user_meter_types(user_id: int, meter_types_ids: List[int]):
        MeterTypeProvider.delete_from_user_meter_types(user_id, meter_types_ids)
