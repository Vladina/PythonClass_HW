def my_dict(**kwargs):
    for key, value in kwargs.items():
        key = key*2
        print(key, value)

my_dict(d = 45, g = 46)


# def my_dict(**kwargs):
#     result = lambda key: key * 2, my_dict
#     print(result)
#
#
# my_dict(d=4, f=7)
# print(my_dict())