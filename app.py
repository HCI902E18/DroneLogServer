import json

from flask import Flask, render_template
from flask.json import jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('map.html')


def battery(level):
    if level is None:
        return 100
    return level


def log_map(data, idx, len_):
    return {
        'lat': data['position']['latitude'],
        'lon': data['position']['longitude'],
        'battery': battery(data['batteryPercent'])
    }


def valid(data):
    return data['position']['latitude'] is not None


@app.route('/log')
def log():
    with open('logs/flight_log.json', 'r') as f:
        points = json.loads(f.read())
        return jsonify([log_map(point, idx, len(points)) for idx, point in enumerate(points) if valid(point)])


if __name__ == '__main__':
    app.run(
        debug=True,
    )
