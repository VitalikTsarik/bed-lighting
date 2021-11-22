from datetime import datetime

from flask import Flask, request, jsonify, render_template
from flask_apscheduler import APScheduler

import led_controller
from effects import Effects
from sunset_helpers import get_sunset_time


class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__, static_folder='frontend/build/static', template_folder='frontend/build')
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)


def turn_on_lights():
    led_controller.lights_on()


scheduler.add_job(id='lights_turn_on', func=turn_on_lights, trigger='cron', hour='20', minute='0')


@scheduler.task(id='lights_turn_off', trigger='cron', minute='0', hour='1')
def turn_off_lights():
    led_controller.lights_off()


@scheduler.task(id='adjust_sunset_time', trigger='cron', minute='0', hour='0', next_run_time=datetime.now())
def adjust_sunset_time():
    sunset = get_sunset_time()
    scheduler.scheduler.reschedule_job(job_id='lights_turn_on', trigger='cron', hour=sunset.hour, minute=sunset.minute)


scheduler.start()


@app.before_first_request
def start_led_watcher():
    led_controller.start()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/led', methods=['POST'])
def led():
    response = {}
    try:
        data = request.json
        color = data.get('color')
        red = color.get('red')
        green = color.get('green')
        blue = color.get('blue')
        effect = data.get('effect')
        led_controller.update(red, green, blue, Effects(effect))

    except Exception as e:
        response['errorMessage'] = e

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
