from timeit import timeit 
import random
import time

def my_method():

    sleep_time = random.randint(1,5)

    time.sleep(sleep_time)

runs = random.randint(1,5)

execution_time = timeit(my_method,number=runs)

message = f'Code ran {runs} times for a total of {execution_time} seconds'
print(message)

