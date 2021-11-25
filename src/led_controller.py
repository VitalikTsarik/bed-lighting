import json
from os import popen

from effects import Effects

WATCHER_PATH = './watcher.py'
STATUS_PATH = './status.json'


def start():
    popen(f'sudo python3 {WATCHER_PATH}')


def stop():
    popen('sudo pkill -f watcher.py')


def lights_on():
    # TODO: make color and effect configurable from frontend
    update(green=180, effect=Effects.SCROLL_OUT)


def lights_off():
    update(0, 0, 0, Effects.SCROLL_OUT)


def update(red=0, green=0, blue=0, effect=Effects.INSTANT):
    with open(STATUS_PATH, 'w', encoding='utf-8') as f:
        json.dump({
            'color': {
                'red': red,
                'green': green,
                'blue': blue,
            },
            'effect': effect.value,
        }, f)


def get_color():
    with open(STATUS_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)
