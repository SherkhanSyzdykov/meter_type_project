from typing import List
import asyncio
from autobahn.asyncio.wamp import ApplicationSession

from .schemas import MeterTypeRead, MeterTypeCreate, MeterTypesList
from .services import MeterTypeQuery
from .models import MeterType


class MeterTypeBackendComponent(ApplicationSession):
    async def onJoin(self, details):
        def get_meter_types():
            orm_meter_types: List[MeterType] = MeterTypeQuery.get().all()
            return MeterTypesList.from_orm(orm_meter_types).json()

        await self.register(get_meter_types, 'get_meter_types')


class MeterTypeFrontendComponent(ApplicationSession):
    async def onJoin(self, details):
        res = await self.call('get_meter_types')
        print(res)

        self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()
