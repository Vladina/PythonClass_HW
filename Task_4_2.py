mylist = [1, 2, 3, 4, 5]
new_list = []
length = len(mylist)
index_number = 0

while index_number < length:
    current_number = mylist[index_number]
    if current_number % 2 == 0:
        new_list.append(current_number)
    index_number += 1

print(len(new_list))

my_list = [1, 2, 3, 4, 5, 6]
my_new_list = []
for i in my_list:
    if i % 2 == 0:
        my_new_list.append(i * -2)
print(len(my_new_list))
