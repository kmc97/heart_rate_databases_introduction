from pymodm import connect
from pymodm import MongoModel, fields
import datetime
import numpy as np

connect("mongodb://localhost:27017/bme590") # connect to database

class User(MongoModel):

    """ class creates user for Mongo Database

    :param email: email of user
    :param age: age of user
    :param heart_rate: heart rate of user
    :heart rate times: prints time of entry
    """
    email = fields.EmailField(primary_key=True)
    age = fields.IntegerField()
    heart_rate = fields.ListField(field=fields.IntegerField())
    heart_rate_times = fields.ListField()

def user_exist(email):

    """ function to check if user exists, if exist returns true

    :param email: email of user
    :returns real_state: state of user id, true= exists
    :raises ValueError: if user does not exist
    """

    try:
        exist = User.objects.raw({"_id": email}).first()
        print("user exists")
        real_state = True
    except:
        print("User DNE")
        real_state = False

    return real_state

def create_new_user(email, age, heart_rate, time):

    """ function to create new user and save entry in database

    :param email: email of user
    :param age: user age
    :param heart_rate: heart rate of user
    :param time: timestamps of entries
    """

    u = User(email, age, [],[])
    u.heart_rate.append(heart_rate)
    u.heart_rate_times.append(time)
    u.save()

def add_heart_rate(email, heart_rate, time):
    
    """function to append data to existing user and saves in database
 
    :param email: email of user
    :param heart_rate: added heart rate of user
    :param time: added timestamp of entry
    """

    u = User.objects.raw({"_id": email}).first() # Get the first user where _id=email
    u.heart_rate.append(heart_rate) # Append the heart_rate to the user's list of heart rates
    u.heart_rate_times.append(time) # append the current time to the user's list of heart rate times
    u.save() # save the user to the database

def return_all_hr(email):
   
    """function returns all heart rates

    :param email: user email
    :returns u.heart_rate: list of heart rates
    """
 
    u = User.objects.raw({"_id": email}).first()
    return u.heart_rate
 

def return_avg_hr(email, heart_rate_values):
 
    """ function returns average of all heart rates
 
    :param email: user email
    :param heart_rate_values: list of heart rate values
    :returns hr_avg: returns hr avg for all heart rate values
    """
 
    hr_avg = np.mean(heart_rate_values)
    return hr_avg    
           
def find_time_index(time_bound,time):

    """function that finds the index of the time stamps based on user input
    
    :param time_bound: time MUST BE IN '%Y-%d-%m %H:%M:%S' format
    :param time: list of timestamps
    :return time_index: the index of the last time stamp
    """

    time_index = None
    for i in range(0, len(time)):
        if time_bound <= time[i]:
            time_index = i
            break
   
    return time_index

def return_interval_hr(time_index, heart_rate):

    """function that returns the average heart rate value in a given interval based on index
    
    :param time_index: integer value representing index of user input-timestamp
    :param heart_rate: heart rates of a given user
    :returns avg_interval_hr: returns average hr value across a user input interval
    """

    hr_list = []
    for i in range(0, len(heart_rate)):
        if i >= time_index:
            hr_list.append(heart_rate[i])
    avg_interval_hr= np.mean(hr_list)
    return avg_interval_hr
        
def obtain_hr_times_list(email):
    
    """function that finds hr and timestamps for a given user

    :params email: user email
    :return list: of heart rates and their respective timestamps
    """

    hr = []
    timestamps = []
    for user in User.objects.raw({"_id": emails}):
        hr.append(user.heart_rate)
        timestamps.append(user.heart_rate_times)
    hr = hr[0]
    timestamps = timestamps[0]       
    return [hr, timestamps]




#timestamp = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#create_new_user( emails, age = 99, heart_rate = 48 , time = timestamp)
#add_heart_rate(emails, heart_rate =21, time = timestamp)

#hr = obtain_hr_times_list(emails)[0]
#timestamps = obtain_hr_times_list(emails)[1]

#index = find_time_index('2018-03-22 14:26:12', timestamps)

#print(return_interval_hr(index, hr))

