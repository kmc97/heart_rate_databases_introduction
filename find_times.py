import numpy as np

def find_time_index(time_bound,time):

    """function that finds the index of the time stamps based on user input

    :param time_bound: time MUST BE IN '%Y-%d-%m %H:%M:%S' format
    :param time: list of timestamps
    :return time_index: the index of the last time stamp
    """
    
    try:
        time_index = None
        for i in range(0, len(time)):
            if time_bound <= time[i]:
                time_index = i
                break

        return time_index
    except:
        print('Error finding time index, ensure time bound input as string %Y-%d-%m %H:%M:%S')

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

def is_tachy(avg_interval_hr, user_age):

    """ function that determines if user is tachy cardic based on wikipedia standards
    
    :param avg_interval_hr: avg heart rate value used in diagnosis
    :param user_age: age of the user to determine if tachycardic
    :returns x: a flag, if x = 1 patient is tachycardic, if x = 0 they are not
    """

    if (user_age >= 1) and (user_age <=2):
        if avg_interval_hr >=151:
            x = 1
            print('Tachycardic')
        else:
            x = 0

    if (user_age >= 3) and (user_age <=4):
        if avg_interval_hr >= 137:
            x = 1
            print('Tachycardic')
        else:
            x = 0

    if (user_age >= 5) and (user_age <=7):
        if avg_interval_hr >= 137:
            x = 1
            print('Tachycardic')
        else:
            x = 0

    if (user_age >= 8) and (user_age <=11):
        if avg_interval_hr >= 130:
            x = 1
            print('Tachycardic')
        else:
            x = 0
    if (user_age >= 12) and (user_age <=15):
        if avg_interval_hr >= 119:
            x = 1
            print('Tachycardic')
        else:
            x = 0
    if (user_age >= 15):
        if avg_interval_hr >= 100:
            x = 1
            print('Tachycardic')
        else:
            x = 0
    return x

def validate_inputs(post):

    """function validates the user inputs from initial post (no missing data, correct format)

    :param post: format {'user_email': ' ', 'user_age': int, 'heart_rate': int
    :raises ValueError: creates value error for incomplete or incorrect data
    """

    if 'user_email' not in post:
        raise ValueError('missing email in post, trya again')
    else:
        if not isinstance(post['user_email'], str):
            raise ValueError('email must be a string in email format')
    
        pass

    if 'heart_rate' not in post:
       raise ValueError('missing heart rate value in post')
    else: 
        if not isinstance(post['heart_rate'], int):
            raise ValueError('Heart Rate must be a single integer')
        pass

    if 'user_age' not in post:
        raise ValueError('missing user age in post')
    else:
        if not isinstance(post['user_age'], int):
            raise ValueError('age must be a single integer')
        pass
