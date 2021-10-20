import asyncio
from autobahn.asyncio.component import Component, run


async def main(reactor, session):
    print('Joined frontend')
    print('Meter types res')
    meter_types_res = await session.call('get_meter_types')
    print('Meter types list res: {}'.format(meter_types_res))
    print()
    print('Meter type res')
    meter_type_res = await session.call('get_meter_type', meter_type_id=1)
    print('Meter type res: {}'.format(meter_type_res))
    print()
    print('Create meter type res')
    create_meter_type_res = await session.call('create_meter_type', json_data='{"name": "test_wamp_json2"}')
    print('Create meter type res: {}'.format(create_meter_type_res))
    print()
    print('Get user meter types')
    get_user_meter_types = await session.call('get_user_meter_types', user_id=1)
    print('Get user meter types res: {}'.format(get_user_meter_types))
    print()
    print('Add to user meter types')
    add_to_user_meter_types = await session.call('add_to_user_meter_types', user_id=1, meter_types_ids=[1, 2])
    print('Add to user meter types res: {}'.format(add_to_user_meter_types))
    print()
    print('Delete from user meter types')
    delete_from_user_meter_types = await session.call('delete_from_user_meter_types', user_id=1, meter_types_ids=[2, 4])
    print('Delete from user meter types res: {}'.format(delete_from_user_meter_types))

    session.leave()


component = Component(transports='ws://localhost:8080/ws', realm='realm1', main=main)


if __name__ == '__main__':
    run([component])
