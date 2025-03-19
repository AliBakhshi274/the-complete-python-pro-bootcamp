import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds")
    return wrapper

@speed_calc_decorator
def fast_func():
    for i in range(100):
        i * i

@speed_calc_decorator
def slow_func():
    for i in range(100):
        i * i

fast_func()
slow_func()




