import pytest
import datetime

def test_time_index():
    from database import find_times
    time_bound = '2018-03-22 12:00:00'
    time = ['2018-02-22 01:00:00', '2017-01-01 12:59:12', '2018-03-24 07:32:12']
    index = find_time_index(time_bound, time)
    assert (index ==1)
