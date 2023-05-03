import logging
import asyncio
import os
from hbmqtt.broker import Broker




logger = logging.getLogger(__name__)
config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': '192.168.0.107:5288',
            'max_connections': 10,
        },
        'ws-mqtt': {
            'type': 'ws',
            'bind': '192.168.0.107:8080',
            'max_connections': 10,
        },
    },
    'sys_interval': 10,
    'auth': {
        'allow-anonymous': True,
        'password-file': os.path.join(os.path.dirname(os.path.realpath(__file__)), "passwd"),
        'plugins': [
            'auth_file', 'auth_anonymous'
        ]
    },
    'topic-check': {
        'enabled': True,
        'plugins': [
            'Try/MQTT'
        ]
    }
}
broker = Broker(config)
@asyncio.coroutine
def test_coro():
    yield from broker.start()


    # yield from asyncio.sleep(5)
    # yield from broker.shutdown()
if __name__ == '__main__':
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    #formatter = "%(asctime)s :: %(levelname)s :: %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(test_coro())
    asyncio.get_event_loop().run_forever()
