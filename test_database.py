import pytest
import datetime
import numpy as np

def test_time_index():
    from find_times import find_time_index
    time_bound = '2018-03-22 12:00:00'
    time = ['2017-02-22 01:00:00', '2017-03-01 12:59:12', '2018-03-24 07:32:12', '2018-06-22 00:00:00']
    index = find_time_index(time_bound, time)
    assert (index ==2)



def test_return_avg_hr():
    from find_times import return_interval_hr
    time_index = 2
    heart_rate = [74, 42,  99, 80, 80, 80]
    avg = return_interval_hr(time_index, heart_rate)
    assert avg == 84.75 


def test_tachy():
    from find_times import is_tachy
    avg_interval_hr = 180
    age1 = 1
    x = is_tachy(avg_interval_hr,age1)
    assert x ==1

    avg_interval1 = 50
    age2 = 49
    x = is_tachy(avg_interval1,age2)
    assert x == 0

    x = is_tachy(234, 24)
    assert x ==1


def test_user_age_validation():
    from find_times import validate_inputs
    data = {'user_email': 'katie@hello.com', 'user_age': 'imnotanage', 'heart_rate': 72}
    data1 = {'user_email': 'katie@hello.com', 'user_age': 27.2, 'heart_rate': 72}
    data2 = {'user_email': 'katie@hello.com', 'heart_rate': 72}
    with pytest.raises(ValueError):
        validate_inputs(data)
        validate_inputs(data1)
        validate_inputs(data2)

def test_user_email_validation():
# mongos db class field thing already makes sure that it is in correct email form
    from find_times import validate_inputs
    data = {'user_age': 12, 'heart_rate': 72}
    data1 = {'user_email': 124 , 'user_age': 32, 'heart_rate': 72}
    with pytest.raises(ValueError):
        validate_inputs(data)
        validate_inputs(data1)

def test_user_hr_validation():
    from find_times import validate_inputs
    data = {'user_email': 'katie@hello.com', 'user_age': 12, 'heart_rate': 'age'}
    data1 = {'user_email': 'katie@hello.com', 'user_age': 12}
    with pytest.raises(ValueError):
        validate_inputs(data)
        validate_inputs(data1)
