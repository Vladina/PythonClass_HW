phrase = input("Enter something: ")


def case_calculator(phrase):
    lower_count = 0
    upper_count = 0
    case_dict = {}
    for i in phrase:
        if i.islower():
            lower_count = lower_count + 1
        elif i.isupper():
            upper_count = upper_count + 1
    case_dict['Upper case characters'] = upper_count
    case_dict['Lower case characters'] = lower_count
    print(case_dict)


case_calculator(phrase)
