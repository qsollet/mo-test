from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

def calculate_ride(hour, distance):
    mile_cost = 2.5
    if hour < 6 or hour >= 20:
        mile_cost = 5
    elif hour >= 16 and hour < 19:
        mile_cost = 7.5
    return 1 + distance * mile_cost
