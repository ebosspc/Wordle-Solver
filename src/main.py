#####-Imports-#####
# Import the math library for mathematical functions
import math as math

# Import random library for random number generation
import random as rand

# Import module that generates the word list
import word_list_generation as word_list_generation

# Import a module to welcome the user
import welcome as welcome

# Import a moduel that processes word data
import word_processing as word_processing

#####-Setup-#####
# Generate a list of all 5 letter words in English and import it
word_list_generation.get_5_letter_words()
from word_list_generation import five_letter_words_list

# Welcome the user to the script
welcome.print_instructions()

#####-Functions-#####
# Define a function to remove impossible words after the first guess
def remove_first_guess_words():
    # Get the first word's data and import it into this module
    word_processing.get_first_word_data()
    word_processing.process_first_word_data()
    global five_letter_words_list, possible_char_1_list, possible_char_2_list, possible_char_3_list, possible_char_4_list, possible_char_5_list
    from word_processing import possible_char_1_list
    from word_processing import possible_char_2_list
    from word_processing import possible_char_3_list
    from word_processing import possible_char_4_list
    from word_processing import possible_char_5_list

    # Remove eliminated words from the possible words list
    for word in five_letter_words_list:
        if word[0] not in possible_char_1_list:
            five_letter_words_list.remove(word)
    for word in five_letter_words_list:
        if word[1] not in possible_char_2_list:
            five_letter_words_list.remove(word)
    for word in five_letter_words_list:
        if word[2] not in possible_char_3_list:
            five_letter_words_list.remove(word)
    for word in five_letter_words_list:
        if word[3] not in possible_char_4_list:
            five_letter_words_list.remove(word)
    for word in five_letter_words_list:
        if word[4] not in possible_char_5_list:
            five_letter_words_list.remove(word)


# Define a function to remove impossible words after the second guess
def remove_second_guess_words():
    # Get the second word's data and import it into this module
    word_processing.get_second_word_data()
    word_processing.process_second_word_data()
    global five_letter_words_list
    from word_processing import possible_char_1_list
    from word_processing import possible_char_2_list
    from word_processing import possible_char_3_list
    from word_processing import possible_char_4_list
    from word_processing import possible_char_5_list
    # Remove eliminated words from the possible words list
    for word in five_letter_words_list:
        if word[0] not in possible_char_1_list:
            five_letter_words_list.remove(word)
    for word in five_letter_words_list:
        if word[1] not in possible_char_2_list:
            five_letter_words_list.remove(word)
    for word in five_letter_words_list:
        if word[2] not in possible_char_3_list:
            five_letter_words_list.remove(word)
    for word in five_letter_words_list:
        if word[3] not in possible_char_4_list:
            five_letter_words_list.remove(word)
    for word in five_letter_words_list:
        if word[4] not in possible_char_5_list:
            five_letter_words_list.remove(word)


# Define a function to remvoed words that should have been removed but didn't
def remove_unremoved_words():
    '''
    This function just does what is already done in other functions
    over and over again. Since the remove function can only remove one element at a time, 
    and there can be multple similar elements, running this function ensures all elements that should be removed get removed
    '''
    global five_letter_words_list
    for i in range(20):
        for word in five_letter_words_list:
            if word[0] not in possible_char_1_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[1] not in possible_char_2_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[2] not in possible_char_3_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[3] not in possible_char_4_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[4] not in possible_char_5_list:
                five_letter_words_list.remove(word)


# Define a function to determine the best thrid word that the user shoudl guess
def grab_third_word():
    global unguessed_letters_list,best_word_char_1,best_word_char_2,best_word_char_3,best_word_char_4,best_word_char_5
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
        if len(five_letter_words_list) == 0:
            print("Sorry there are no possible word combinations with the data you entered")
            quit()
        else:
            best_word = rand.choice(five_letter_words_list)

    if len(five_letter_words_list) != 0:
        # Split up the best word into 5 variables, each containing one of its characters
        best_word_char_1 = best_word[0]
        best_word_char_2 = best_word[1]
        best_word_char_3 = best_word[2]
        best_word_char_4 = best_word[3]
        best_word_char_5 = best_word[4]


#####-Processing-#####
# Remove eliminated words from the possible words list after the first 2 guesses using preset words
remove_first_guess_words()
print(len(five_letter_words_list))
remove_second_guess_words()
print(len(five_letter_words_list))

# Remove any remaining words the algorithm may have missed
remove_unremoved_words()
grab_third_word()
print(best_word_char_1,best_word_char_2,best_word_char_3,best_word_char_4,best_word_char_5)

print(len(five_letter_words_list))
print(five_letter_words_list)
