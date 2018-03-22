import numpy as np
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



