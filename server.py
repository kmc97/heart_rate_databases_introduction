from database import return_all_hr, return_avg_hr, user_exist, create_new_user, add_heart_rate
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



@app.route('/api/heart_rate', methods = ['POST'])
def received_data():
    r = request.get_json()
    email = r["user_email"]
    age = r["user_age"]
    heart_rate = r["heart_rate"]

    try:
        user_exist(email)
        add_heart_rate(email,heart_rate, datetime.datetime.now())
    
    except:
        print('user DNE')
        create_new_user(email, age, heart_rate, datetime.datetime.now())
    
    print_vals = {
        "user_email": email,
        "user_age": age,
        "heart_rate": heart_rate
    }
    return jsonify(print_vals)
    

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
        "heart_rate": return_avg_hr(user_email, hr)

    }
    return jsonify(avg_hr)
