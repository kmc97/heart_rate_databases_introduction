from pymodm import connect
from pymodm import MongoModel, fields
from datetime import datetime

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
    """

    try:
        exist = User.objects.raw({"_id": email}).first()
        real_state = True
    except:
        print("User DNE")
        real_state = False

    return real_state

def create_user(email, age, heart_rate, time):
    u = User(email, age, [],[])
    u.heart_rate.append(heart_rate)
    u.heart_rate_times.append(time)
    u.save()


create_user('katierox@email.com', age = 99, heart_rate = 48 , time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
user_exist('katierox@email.com')


for user in User.objects.raw({"age":99}):
    print(user.heart_rate_times)
