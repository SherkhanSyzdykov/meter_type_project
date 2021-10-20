from os import environ
from autobahn.asyncio.wamp import ApplicationRunner

from meter_type.components import MeterTypeBackendComponent


if __name__ == '__main__':
    url = environ.get("AUTOBAHN_DEMO_ROUTER", "ws://127.0.0.1:8080/ws")
    realm = "realm1"
    runner = ApplicationRunner(url, realm)
    runner.run(MeterTypeBackendComponent)
