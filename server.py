from database import return_all_hr, return_avg_hr
import datetime
from flask import Flask, jsonify, request
from pymodm import connect

app = Flask(__name__)
connect("mongodb://localhost:27017/bme590")

@app.route('/', methods = ['GET'])
def hello():
    hr = {
        "name": 'Hello there'
    }
    return jsonify(hr)

@app.route('/api/heart_rate/<user_email>', methods = ['GET'])
def get_hr(user_email):
    hr = {
        "hr" : return_all_hr(user_email)
    }
    return jsonify(hr)
    

@app.route('/api/heart_rate/average/<user_email>', methods = ['GET'])
def get_avg_hr(user_email):
    hr = return_all_hr(user_email)
    avg_hr= {
        "heart_rate": return_all_hr(user_email)

    }
    return jsonify(avg_hr)
