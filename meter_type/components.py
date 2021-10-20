from typing import List
from autobahn.asyncio.component import Component

from .schemas import MeterTypeCreate, MeterTypesList
from .services import MeterTypeService


component = Component(
    transports='ws://localhost:8080/ws',
    realm='realm1'
)


@component.on_join
async def joined(session, details):
    print('Session ready')


@component.on_leave
async def left(session, details):
    print('Session close')


@component.register('get_meter_types')
async def get_meter_types() -> str:
    return MeterTypeService.get_meter_types().json()


@component.register('get_meter_type')
async def get_meter_type(meter_type_id: int) -> str:
    return MeterTypeService.get_meter_type(meter_type_id).json()


@component.register('create_meter_type')
async def create_meter_type(json_data: str):
    meter_type = MeterTypeCreate.parse_raw(json_data)
    MeterTypeService.create_meter_type(meter_type)


@component.register('get_user_meter_types')
async def get_user_meter_types(user_id: int) -> str:
    return MeterTypeService.get_user_meter_types(user_id).json()


@component.register('add_to_user_meter_types')
async def add_to_user_meter_types(user_id: int, meter_types_ids: List[int]):
    MeterTypeService.add_to_user_meter_types(user_id, meter_types_ids)


@component.register('delete_from_user_meter_types')
async def delete_from_user_meter_types(user_id: int, meter_types_ids: List[int]):
    MeterTypeService.delete_from_user_meter_types(user_id, meter_types_ids)
