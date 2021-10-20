from autobahn.asyncio.component import Component, run


component = Component(transports='ws://localhost:8080/ws', realm='realm1')


@component.on_join
async def joined(session, details):
    print('Joined frontend')
    meter_types_res = await session.call('get_meter_types')
    print('Meter types list res: {}'.format(meter_types_res))
    create_meter_type_res = await session.call('create_meter_type', json_data='{"name": "test_wamp_json1"}')
    print('Create meter type res: {}'.format(create_meter_type_res))
    await session.leave()


if __name__ == '__main__':
    run([component])
