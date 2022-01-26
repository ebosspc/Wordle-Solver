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
    global five_letter_words_list,possible_char_1_list,possible_char_2_list,possible_char_3_list,possible_char_4_list,possible_char_5_list
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
    over and over again because python isn't 100% accurate with scanning lists.
    Why does this happen? I have no idea. 
    I just found that by continuously running the code segment, 
    Python is able to catch all of the words it missed.
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


#####-Processing-#####
# Remove eliminated words from the possible words list after the first 2 guesses using preset words
remove_first_guess_words()
print(len(five_letter_words_list))
remove_second_guess_words()
print(len(five_letter_words_list))

# Remove any remaining words the algorithm may have missed
remove_unremoved_words()


print(len(five_letter_words_list))
print(five_letter_words_list)
