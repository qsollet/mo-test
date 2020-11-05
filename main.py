from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

def calculate_ride(hour, distance):
    price = 1 # starting price
    price += distance * 2.5 # distance cost
    return price
