# python3 1-timer.py

from custom_decorator import *

@timer
def waste_time(num):
    for _ in range(num):
        sum([i**2 for i in range(10000)])

waste_time(1)
waste_time(999)