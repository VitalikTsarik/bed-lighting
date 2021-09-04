from suntime import Sun

latitude = 53.9
longitude = 27.5


def get_sunset_time():
    sun = Sun(latitude, longitude)
    return sun.get_local_sunset_time()
