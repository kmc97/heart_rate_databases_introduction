from pymodm import connect
from pymodm import MongoModel, fields
import datetime
import numpy as np

connect("mongodb://localhost:27017/bme590") # connect to database
emails = ('katierox@email.com')

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
    u = User(email, age, [],[])
    u.heart_rate.append(heart_rate)
    u.heart_rate_times.append(time)
    u.save()
    print("user created")

def add_heart_rate(email, heart_rate, time):
    u = User.objects.raw({"_id": email}).first() # Get the first user where _id=email
    u.heart_rate.append(heart_rate) # Append the heart_rate to the user's list of heart rates
    u.heart_rate_times.append(time) # append the current time to the user's list of heart rate times
    u.save() # save the user to the database

def return_all_hr(email): 
    u = User.objects.raw({"_id": email}).first()
    return u.heart_rate
 

def return_avg_hr(email, heart_rate_values): 
    hr_avg = np.mean(heart_rate_values)
    return hr_avg    


def return_avg_since(email, time_since):
    u = User.objects.raw({"_id":email}).first()
    hr_since = u.heart_rate(since_time= time_since)
    avg_since = np.mean(avg_since)
    print(avg_since)
    

#create_new_user('katierox@email.com', age = 99, heart_rate = 48 , time = datetime.datetime.now())
for user in User.objects.raw({"_id": 'suyash@suyashkumar.com'}):
    print(user.heart_rate_times)

#user_exist(emails)
#return_all_hr(emails)
#print(return_avg_hr(emails, hr_values))
#return_avg_since(emails,datetime.datetime.now())
