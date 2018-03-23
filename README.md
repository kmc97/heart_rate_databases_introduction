# heart_rate_databases_introduction

[![Build Status](https://travis-ci.org/kmc97/heart_rate_databases_introduction.svg?branch=master)](https://travis-ci.org/kmc97/heart_rate_databases_introduction)

This code is to be used on a virtual machine and utilizes the starter codebase for BME590 Databases Assignment (which can be found [here](https://github.com/mlp6/Medical-Software-Design/blob/master/Lectures/databases/main.md#mini-projectassignment)). 

To get started with this code, you first need to get the mongodb program running. To do this, simply run 
``` 
docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```
once your database is running and your connection string is set, you can run the starter program by running `main.py` after activating your `virtualenv` and installing all the dependencies listed in `requirements.txt`.

to run server you need to set up the GUNICORN connection:
```
gunicorn --bind 0.0.0.0:5000 server:app
```

The following programs are in the repository:

server.py: the program that is run with GUNICORN, the backend server for this project. It has 4 possible GET/POST connections detailed below
- POST api/heart_rate (which stores a user post into the MongosDB database):
    data must be entered as
```  
data = {
        "user_email": "suyash@suyashkumar.com",
        "user_age": 50, // in years
        "heart_rate": 100
    }
  ```  
- GET /api/heart_rate/<user_email> (returns all hr for a given user)
- GET /api/heart_rate/average/<user_email> (returns avg heart rate over all users)
- POST /api/heart_rate/interval_average (returns avg heart rate over user specified interval AND if user is tachycardic). this program works in my tests but couldnt quite get it to work over the server, im not sure what the error means.
    data must be entered as *NOTE this program does not expect the float at the end of timestamp*:
   
   ```
   data = {
        "user_email": "",
        "heart_rate_average_since": "2018-03-09 11:00:36"
    }
   ``` 
database.py: contains functions that interact with mongosDB. server pulls these functions

find_times.py: contains functions that *DONT* interact with mongosDB (easier to test). server pulls functions

client.py: used to test server

test_database.py: tests find_times (functions that do not interact with FLASK or MONGOSdb)
    - testing only works on the local computer NOT the virtualenv (because we like to make things easy)    

requirements.txt: pip3 install into virtualenv

ENJOY!
