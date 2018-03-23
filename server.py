from database import return_all_hr, return_avg_hr, user_exist, create_new_user, add_heart_rate, obtain_hr_times_list
from find_times import find_time_index, return_interval_hr, is_tachy, validate_inputs
import datetime
from flask import Flask, jsonify, request
from pymodm import connect

app = Flask(__name__)
connect("mongodb://localhost:27017/bme590")


@app.route('/api/heart_rate', methods = ['POST'])

def received_data():
    """ Function takes in json post from user, validates the input from the user, checks if user exists and enters data into database
    
    :param r: json file that contains email, age, heart_rate
    :returns: json string of email, age, heart_rate
    """

    r = request.get_json()
    validate_inputs(r)

    email = r["user_email"]
    age = r["user_age"]
    heart_rate = r["heart_rate"]

    try:
        user_exist(email)
        add_heart_rate(email,heart_rate, datetime.datetime.now())
    
    except:
        create_new_user(email, age, heart_rate, datetime.datetime.now())
   
 
    print_vals = {
        "user_email": email,
        "user_age": age,
        "heart_rate": heart_rate
    }
    return jsonify(print_vals), 200
    

@app.route('/api/heart_rate/<user_email>', methods = ['GET'])
def get_hr(user_email):
    """Function makes sure user exists before retreiving all hr for a given user

    :param user_email: user email
    :returns hr: all hr values for user   
    """
 
    try:
        user_exist(email)
        hr = {
            "all hr" : return_all_hr(user_email)
        }

        return jsonify(hr), 200

    except:
        return 400
    

@app.route('/api/heart_rate/average/<user_email>', methods = ['GET'])
def get_avg_hr(user_email):
    """Function makes sure user exists before getting average heart across all hr values for a given user

    :param user_email: user email
    :returns avg_hr: average heart rate across all hrs of user
    """

    try:
        user_exist(email)
        hr = return_all_hr(user_email)
        avg_hr= {
            "heart_rate": return_avg_hr(user_email, hr)

        }
        return jsonify(avg_hr), 200

    except:
        return 400


@app.route('/api/heart_rate/interval_average', methods = ['POST'])
def post_interval_hr():
    """ Function takes in user posted email and specific cutt_off time and returns avg hr. Function makes sure that the user exists, pulls additional data from mongos db and determines if tachy cardic

    :param time_cuttoff: time must be string entered in '%Y-%m-%d %H:%M:%S'format
    :param user_email: user email
    :param x: if 1 user is tachycardic, if 0 user is not tachycardic
    :returns print_vals: average hr interval, the cuttoff time and if patient is tachycardic
    """
   
    try:
        r = request.get_json()
        email = r["user_email"]
        time_cuttoff = r["heart_rate_average_since"]  
        user_exists(email)  


        hr = obtain_hr_times_list(email)[0]
        timestamps = obtain_hr_times_list(email)[1]
        age = obtain_hr_times(email)[2]

        index = find_time_index(time_cuttoff, timestamps)
        hr_int = return_interval_hr(index, hr_int)    

        x= is_tachy(hr_int, age)

        if (x == 1):
            status = 'Alert Tachycardic'
        else:
            status= 'not tachycardic'

        print_vals = {
            "avg_hr_interval" : hr_int,
            "heart_rate_average_since": time_cuttoff,
            "tachycardic?" :status
        }

        return jsonify(print_vals), 200

    except:
        return 400
    
