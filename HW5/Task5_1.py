a = ''
a_init = "*"
i = 0
word = '*****'
stop = len(word)
for i in range(0, 5):
    i += 1
    a += a_init
    print(a)
for i in word:
    stop -= 1
    print(word[:stop])




# word = input()
# for char in word:
#     print(char)





