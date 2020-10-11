def my_decorator(func):
    def wrapper(arg1, arg2):
        func(arg2, arg1)

    return wrapper


@my_decorator
def my_func(name, age):
    print(name, age)


my_func('Dina', 37)
