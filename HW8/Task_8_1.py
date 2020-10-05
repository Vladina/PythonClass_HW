unique_list = []


def func(list_):
    for i in list_:
        if list_.count(i) == 1:
            unique_list.append(i)
        else:
            pass
    print(unique_list)


func([1, 2, 2, 4, 5, 5, 3, 'g', 'h', 'g'])
