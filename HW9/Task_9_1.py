word = 'dfas;fj a;g'
word_list = [str(i) for i in word]
new_word_list = [f'{word_list.index(i)} - {i}' for i in word_list ]
print(new_word_list)