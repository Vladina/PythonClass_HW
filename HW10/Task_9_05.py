import functools
from functools import reduce


# another way of a function definition:
# def my_func(x, y):
#     while x % 3 == 0:
#         if y % 3 != 0:
#             print('You cannot divide this number by 3')
#             break
#         else:
#             return x*y

def my_func(x, y):
    if x % 3 != 0 or y % 3 != 0:
        print('You cannot divide this number by 3')
    else:
        return x * y


# for numbers multiple of three:
items = ([3, 3, 6, -3])
print(reduce(my_func, items))

# for numbers when not all of them multiple of three:
items = ([3, 3, 6, 5])
print(reduce(my_func, items))

