def my_decorator(func):
    def wrapper(arg):
        for i in arg:
            if i % 2 == 0:
                result = arg.remove(i)
            else:
                pass
        print(arg)
    return wrapper


@my_decorator
def my_func(arg):
    pass


lis = [1, 2, 3, 4, 5, 10, 77]
my_func(lis)

