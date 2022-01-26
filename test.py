import random as rand

word1 = ['a','d','i','e','u'] # score = 0
word2 = ['s','c','o','o','p'] # score = 1
word3 = ['b','e','a','s','t'] # score = 2
word4 = ['s','u','g','a','r'] # score = 3

five_letter_words_list = [word1,word2,word4,word3]

# Create a list of all of the letters that have not been guessed
unguessed_letters_list = ['b','f','g','h','j','k','m','n','p','q','r','t','v','w','x','y','z']

# Define variables to track word sorting
best_word = ['',0]
current_score = 0

# Sort each word based on how many characters it has in that haven't been guess yet
for word in five_letter_words_list:
    if word[0] in unguessed_letters_list:
        current_score += 1
    if word[1] in unguessed_letters_list:
        current_score += 1
    if word[2] in unguessed_letters_list:
        current_score += 1
    if word[3] in unguessed_letters_list:
        current_score += 1
    if word[4] in unguessed_letters_list:
        current_score += 1
    if current_score > best_word[1]:
        best_word.clear()
        best_word.append(word)
        best_word.append(current_score)
    current_score = 0

# Extract the best word from the sorting algorithm
if best_word[1] > 0:
    best_word = best_word[0]
else:
    print("No more unused characters, random word from possible words chosen.")
    best_word = rand.choice(five_letter_words_list)

print(best_word)
    
