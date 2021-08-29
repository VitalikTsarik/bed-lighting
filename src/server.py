from flask import Flask, current_app, url_for, request, jsonify

from led_controller import update_led, start_visualization

app = Flask(__name__)


@app.before_first_request
def start_led_watcher():
    start_visualization()


@app.route('/')
def index():
    return current_app.send_static_file('index.html')


@app.route('/color', methods=['POST'])
def led():
    try:
        data = request.json
        red = data.get('r')
        green = data.get('g')
        blue = data.get('b')
        resp = update_led(red, green, blue)
    except ValueError:
        resp = 'missing required param (red, green, blue)'

    return jsonify({'message': resp})


with app.test_request_context():
    url_for('static', filename='styles.css')
    url_for('static', filename='form.js')
