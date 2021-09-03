import json
from os import popen

WATCHER_PATH = './watcher.py'
STATUS_PATH = './status.json'


def update_color_status(red, green, blue):
    try:
        with open(STATUS_PATH, 'w', encoding='utf-8') as f:
            json.dump({'red': red, 'green': green, 'blue': blue}, f)
    except OSError:
        return 'failed'

    return 'success'


def get_color_status():
    with open(STATUS_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def start_visualization():
    popen(f'sudo python3 {WATCHER_PATH}')


def stop_visualization():
    popen('sudo pkill -f watcher.py')


def is_watching():
    resp = popen('ps aux | grep watcher.py')
    return f'python3 {WATCHER_PATH}' in resp.read()
