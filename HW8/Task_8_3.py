word1 = input('Enter the first word: ')
word2 = input('Enter the second word: ')
word3 = input('Enter the third word: ')
word_list = []
def is_palindrome(word_list):
    word_list = [word1, word2, word3]
    for word in word_list:
        if word == word[::-1]:
            print(f'The {word} word is a palindrome')
        else:
            pass
    return word


is_palindrome(word_list)
