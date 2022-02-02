word_list = []
known_letters_list = ['e','l']
word1 = ['h','e','l','l','o']
word2 = ['a','d','i','e','u']
word3 = ['c','l','o','y','s']
word4 = ['w','r','u','n','g']
word_list.append(word1)
word_list.append(word2)
word_list.append(word3)
word_list.append(word4)

for i in range(len(word_list)):
    for letter in known_letters_list:
        for word in word_list:
            if letter not in word:
                word_list.remove(word)

print(word_list)