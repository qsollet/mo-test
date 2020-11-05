from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/v1/rides', methods=['POST'])
def api_ride():
    rides = request.get_json()['rides']
    for ride in rides:
        ride['cost'] = calculate_ride(
            datetime.strptime(ride['startTime'], '%Y-%m-%dT%H:%M:%S.%fZ').hour,
            ride['distance']
        )
    return jsonify(rides=rides)

def calculate_ride(hour, distance):
    mile_cost = 2.5
    if hour < 6 or hour >= 20:
        mile_cost = 5
    elif hour >= 16 and hour < 19:
        mile_cost = 7.5
    return 1 + distance * mile_cost
