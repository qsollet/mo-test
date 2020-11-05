from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/v1/ride')
def api_ride():
    return 'api call'

def calculate_ride(hour, distance):
    mile_cost = 2.5
    if hour < 6 or hour >= 20:
        mile_cost = 5
    elif hour >= 16 and hour < 19:
        mile_cost = 7.5
    return 1 + distance * mile_cost
