from typing import List
from autobahn.asyncio.component import Component

from .schemas import MeterTypeCreate, MeterTypesList
from .services import MeterTypeQuery
from .models import MeterType
from .provider import MeterTypeProvider


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
    orm_meter_types: List[MeterType] = MeterTypeQuery.get().all()
    return MeterTypesList.from_orm(orm_meter_types).json()


@component.register('create_meter_type')
async def create_meter_type(json_data: str):
    meter_type = MeterTypeCreate.parse_raw(json_data)
    MeterTypeProvider.create(**meter_type.dict())
