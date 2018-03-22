from database import return_all_hr, return_avg_hr, user_exist, create_new_user, add_heart_rate, obtain_hr_times_list
from find_times import find_time_index, return_interval_hr
import datetime
from flask import Flask, jsonify, request
from pymodm import connect

app = Flask(__name__)
connect("mongodb://localhost:27017/bme590")


@app.route('/api/heart_rate', methods = ['POST'])

def received_data():
    """ Function takes in json post from user, checks if user exists and enters data into database
    
    :param r: json file that contains email, age, heart_rate
    :returns: json string of email, age, heart_rate
    """

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
        return 400
 
    print_vals = {
        "user_email": email,
        "user_age": age,
        "heart_rate": heart_rate
    }
    return jsonify(print_vals), 200
    

@app.route('/api/heart_rate/<user_email>', methods = ['GET'])
def get_hr(user_email):
    """Function retreives all hr for a given user

    :param user_email: user email
    :returns hr: all hr values for user   
    """
 
    try:
        user_exist(email)
        hr = {
            "hr" : return_all_hr(user_email)
        }
    except:
        print('please create the user first')
        return 400
    return jsonify(hr), 200
    

@app.route('/api/heart_rate/average/<user_email>', methods = ['GET'])
def get_avg_hr(user_email):
    """Function retreives average heart across all hr values for a given user

    :param user_email: user email
    :returns avg_hr: average heart rate across all hrs of user
    """

    try:
        user_exist(email)
        hr = return_all_hr(user_email)
        avg_hr= {
            "heart_rate": return_avg_hr(user_email, hr)

        }
    except:
        print('please create the user first')
        return 400

    return jsonify(avg_hr), 200

@app.route('/api/heart_rate/interval_average', methods = ['POST'])
def post_interval_hr():
    """ Function takes in user posted email and specific cutt_off time and returns avg hr

    :param time_cuttoff: time must be string entered in '%Y-%m-%d %H:%M:%S'format
    :param user_email: user email
    :returns print_vals: average hr interval and the cuttoff time
    """
   
    try:
        r = request.get_json()
        email = r["user_email"]
        time_cuttoff = r["heart_rate_average_since"]  
  
        hr = obtain_hr_times_list(email)[0]
        timestamps = obtain_hr_times_list(email)[1]
        age = obtain_hr_times(email)[2]
        index = find_time_index(time_cuttoff, timestamps)
        hr_int = return_interval_hr(index, hr_int)    

        is_tachy(hr_int, age)
        if (x == 1):
            status = 'Alert Tachycardic'
        else:
            status= 'not tachycardic'

        print_vals = {
            "avg_hr_interval" : hr_int,
            "heart_rate_average_since": time_cuttoff,
            "tachycardic?" :status
        }
    except:
        print('please create the user first')
        return 400

    return jsonify(print_vals),200
    
    
