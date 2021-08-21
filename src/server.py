from flask import Flask, current_app, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return current_app.send_static_file('index.html')


with app.test_request_context():
    url_for('static', filename='styles.css')
