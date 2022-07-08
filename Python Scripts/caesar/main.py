# word = input('Word : ')
# Making the word in to a list
# print(list(word))

# dictionary = list("abcdefghijklmnopqrstuvwxyz")
# print(dictionary)

def caesar(word, num):
    new_word=[]
    dictionary = list("abcdefghijklmnopqrstuvwxyz")
    word = word.lower()
    word = word.replace(" ", "_")
    list_word=list(word)

    for i in list_word:

        if i == '_':
            new_word.append(" ")

        elif i in dictionary and i != '_':
            # print(f'The index of {i} is {dictionary.index(i)}')
            index = int(dictionary.index(i))
            new_index = index + num
            if new_index > 25:
                new_index1 = int(new_index) % 26
                i = dictionary[new_index1]
                new_word.append(i)
            elif int(new_index) <= 25:
                i = dictionary[new_index]
                new_word.append(i)

    return print(''.join(new_word))

def uncaesar(word, num):
    new_word=[]
    dictionary = list("abcdefghijklmnopqrstuvwxyz")
    word = word.lower()
    word = word.replace(" ", "_")
    list_word=list(word)

    for i in list_word:

        if i == '_':
            new_word.append(" ")

        elif i in dictionary and i != '_':
            # print(f'The index of {i} is {dictionary.index(i)}')
            index = int(dictionary.index(i))
            new_index = index - num
            if new_index <= 25:
                new_index1 = int(new_index) % 26
                i = dictionary[new_index1]
                new_word.append(i)
            elif int(new_index) <= 25:
                i = dictionary[new_index]
                new_word.append(i)

    return print(''.join(new_word))



uncaesar(input('please enter the word : '),int(input('please enter the number : ')))