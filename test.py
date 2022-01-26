letters_list = ['b','f','g','h','j','k','m','n','p','q','r','t','v','w','x','y','z']

word1 = ['a','d','i','e','u'] # score = 0
word2 = ['s','c','o','o','p'] # score = 1
word3 = ['b','e','a','s','t'] # score = 2
word4 = ['s','u','g','a','r'] # score = 3

words_list = [word1,word2,word3,word4]

best_word = ['',0]
current_score = 0

for word in words_list:
    if word[0] in letters_list:
        current_score += 1
    if word[1] in letters_list:
        current_score += 1
    if word[2] in letters_list:
        current_score += 1
    if word[3] in letters_list:
        current_score += 1
    if word[4] in letters_list:
        current_score += 1
    if current_score >= best_word[1]:
        best_word[0] = word
        best_word[1] = current_score

print(best_word[0])
    
