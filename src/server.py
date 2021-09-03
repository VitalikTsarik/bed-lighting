from datetime import datetime

from flask import Flask, current_app, url_for, request, jsonify
from flask_apscheduler import APScheduler

from led_controller import update_color_status, start_visualization, get_color_status


class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)


@scheduler.task('cron', id='sunset', minute='*')
def turn_on_lights():
    status = get_color_status()

    if status['red'] == 10:
        update_color_status(0, 0, 10)
    else:
        update_color_status(10, 0, 0)


scheduler.start()


@app.before_first_request
def start_led_watcher():
    start_visualization()


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
        error = update_color_status(red, green, blue)
        if error:
            response['errorMessage'] = error

    except ValueError:
        response = 'missing required param (red, green, blue)'

    response['localTime'] = datetime.now()

    return jsonify(response)


with app.test_request_context():
    url_for('static', filename='styles.css')
    url_for('static', filename='form.js')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
