import requests

def get_data():
    r = requests.get("http://vcm-3672.vm.duke.edu:5000/")
    data = r.json()
    print(data)

def getsum_data():
    r = requests.get("http://vcm-3672.vm.duke.edu:5000/api/heart_rate/katierox@email.com")
    data = r.json()
    print(data)

def getter_data():
    r = requests.get("http://vcm-3672.vm.duke.edu:5000/api/heart_rate/average/katierox@email.com")
    data = r.json()
    print(data)

def post_data():
    data = {
        "user_email": "katierox@email.com",
        "user_age": 50,
        "heart_rate": 190
    }

    r = requests.post("http://vcm-3672.vm.duke.edu:5000/api/heart_rate", json=data)
    data = r.json()
    print(data)
post_data() 
getsum_data()
getter_data()
