import requests


def get_hr():
    r = requests.get("http://vcm-3672.vm.duke.edu:5000/api/heart_rate/katierox@email.com")
    try:
        data = r.json()
        print(data)
    except:
        print('not receiving data, try again in a bit')

def get_hr_avg():
    r = requests.get("http://vcm-3672.vm.duke.edu:5000/api/heart_rate/average/katierox@email.com")
    try:
        data = r.json()
        print(data)
    except:
         print('not receiving data, try resubmitting, because sometimes it decides to work')

def post_data():
    data = {
        "user_email": "katierox@email.com",
        "user_age": 50,
        "heart_rate": 190
    }

    r = requests.post("http://vcm-3672.vm.duke.edu:5000/api/heart_rate", json=data)
    try: 
        data = r.json()
        print(data)
    except:
        print('not recieving data, try again in a bit this server seems to work sometimes')

def post_interval():
    data = {
        "user_email": "katierox@email.com",
        "heart_rate_average_since": "2018-03-22 11:00:36"
    } 
 
    r = requests.post("http://vcm-3672.vm.duke.edu:5000/api/heart_rate/interval_average", json=data)
    try: 
        data = r.json()
        print(data)
    except:
        print('not receiving data, try again in a bit this server seems to work sometimes :)')

post_data() 
#get_hr()
#get_hr_avg()
#post_interval()
