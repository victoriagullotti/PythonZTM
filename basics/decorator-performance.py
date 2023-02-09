#Use decorator for function performance testing
from time import time

def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        results = fn(*args, **kawrgs)
        t2 = time()

        print(f'It took {t2-t1} s')
        return results
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        1*5

long_time()

#It took 3.3819775581359863 s