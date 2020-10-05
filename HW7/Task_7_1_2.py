user_key = int(input('Enter conversion type: '))
user_number = int(input('Enter a value you want to convert: '))
a = user_number


def convert_to_centimeters(a):
    if isinstance(a, int):
        b = a * 2.54
        print(f'{a} inches is {b} cm')
        return b
    elif isinstance(a, float):
        b = a * 2.54
        print(f'{a} inches is {b} cm')
        return b
    else:
        print("Enter numeric value.")


# convert_to_centimeters(a)


def convert_to_inches(a):
    if isinstance(a, int):
        b = a / 2.54
        print(f'{a} cm is {b} inches')
        return b
    elif isinstance(a, float):
        b = a / 2.54
        print(f'{a} cm is {b} inches')
        return b
    else:
        print("Enter numeric value.")


# convert_to_inches(a)

def convert_to_kilometers(a):
    if isinstance(a, int):
        b = a * 1.609
        print(f'{a} miles is {b} km')
        return b
    elif isinstance(a, float):
        b = a * 1.609
        print(f'{a} miles is {b} km')
        return b
    else:
        print("Enter numeric value.")


# convert_to_kilometers(1.24)

def convert_to_miles(a):
    if isinstance(a, int):
        b = a / 1.609
        print(f'{a} km is {b} miles')
        return b
    elif isinstance(a, float):
        b = a / 1.609
        print(f'{a} km is {b} miles')
        return b
    else:
        print("Enter numeric value.")


# convert_to_miles(12)


functions_lib = {1: convert_to_centimeters(a),
                 2: convert_to_inches(a),
                 3: convert_to_kilometers(a),
                 4: convert_to_miles(a)
                 }
while user_key in functions_lib.keys():
    functions_lib[user_key]
    print(functions_lib[user_key])
    print('Enter 0 to exit a program')
    user_key = int(input('Enter conversion type: '))
    user_number = int(input('Enter a value you want to convert: '))
    a = user_number
    if user_key == 0:
        break





