import json
from os import popen

WATCHER_PATH = './watcher.py'
STATUS_PATH = './status.json'


def start():
    popen(f'sudo python3 {WATCHER_PATH}')


def stop():
    popen('sudo pkill -f watcher.py')


def lights_on():
    update_color(green=10)


def lights_off():
    update_color(0, 0, 0)


def update_color(red=0, green=0, blue=0):
    with open(STATUS_PATH, 'w', encoding='utf-8') as f:
        json.dump({'red': red, 'green': green, 'blue': blue}, f)


def get_color():
    with open(STATUS_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)
