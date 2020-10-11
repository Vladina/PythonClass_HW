from datetime import datetime

time = datetime.now()


def timer(func):
    def wrapper(*args):
        start = time
        func(*args)
        end = time
        print('Function execution takes', end - start, 'seconds.')

    return wrapper


@timer
def my_func(x, y):
    if x % 3 != 0 or y % 3 != 0:
        print('You cannot divide this number by 3')
    else:
        return x * y


print(my_func(166, 999))
