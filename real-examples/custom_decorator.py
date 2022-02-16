
""" [DECORATOR TEMPLATE]

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

"""


import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        # Do something after
        end = time.perf_counter()
        finsih_time = end-start
        print(f"Finished {func.__name__!r} in {finsih_time:.4f} seconds")
        return value
    return wrapper_timer