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

getsum_data()
