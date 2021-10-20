import asyncio
from autobahn.asyncio.component import Component, run


async def main(reactor, session):
    print('Joined frontend')
    meter_types_res = await session.call('get_meter_types')
    print('Meter types list res: {}'.format(meter_types_res))
    create_meter_type_res = await session.call('create_meter_type', json_data='{"name": "test_wamp_json2"}')
    print('Create meter type res: {}'.format(create_meter_type_res))
    session.leave()


component = Component(transports='ws://localhost:8080/ws', realm='realm1', main=main)


if __name__ == '__main__':
    run([component])
