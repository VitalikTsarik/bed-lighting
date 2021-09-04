from datetime import datetime

from flask import Flask, current_app, url_for, request, jsonify
from flask_apscheduler import APScheduler

import led_controller
from sunset_helpers import get_sunset_time


class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)


def turn_on_lights():
    led_controller.lights_on()


scheduler.add_job(id='lights_turn_on', func=turn_on_lights, trigger='cron', hour='20', minute='0')


@scheduler.task(id='lights_turn_off', trigger='cron', minute='0', hour='1')
def turn_off_lights():
    led_controller.lights_off()


@scheduler.task(id='adjust_sunset_time', trigger='cron', minute='0', hour='0')
def adjust_sunset_time():
    sunset = get_sunset_time()
    scheduler.scheduler.reschedule_job(id='lights_turn_on', trigger='cron', hour=sunset.hour, minute=sunset.minute)


scheduler.start()


@app.before_first_request
def start_led_watcher():
    led_controller.start()


@app.route('/')
def index():
    return current_app.send_static_file('index.html')


@app.route('/color', methods=['POST'])
def led():
    response = {}
    try:
        data = request.json
        red = data.get('r')
        green = data.get('g')
        blue = data.get('b')
        led_controller.update_color(red, green, blue)

    except Exception as e:
        response['errorMessage'] = e

    response['localTime'] = datetime.now()

    return jsonify(response)


with app.test_request_context():
    url_for('static', filename='styles.css')
    url_for('static', filename='form.js')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
