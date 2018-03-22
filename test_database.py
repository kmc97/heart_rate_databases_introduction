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
    heart_rate = [74, 42,  99, 82, 132, 70]
    avg = return_interval_hr(time_index, heart_rate)
### #   assert (avg == np.mean([82,132,70])
