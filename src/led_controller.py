import json
import subprocess
from os import popen

WATCHER_PATH = "./watcher.py"
STATUS_PATH = "./status.json"
print(WATCHER_PATH)
print(STATUS_PATH)
with open(STATUS_PATH) as f:
    print(json.load(f))


def update_led(red, green, blue):
    try:
        json.dump({'red': red, 'green': green, 'blue': blue}, open(STATUS_PATH, 'w'))
    except OSError:
        return 'failed'

    return 'success'


def start_visualization():
    subprocess.Popen(['sudo', 'python3', WATCHER_PATH])


def stop_visualization():
    popen('sudo pkill -f watcher.py')


def is_watching():
    resp = popen('ps aux | grep watcher.py')
    return f'python3 {WATCHER_PATH}' in resp.read()
