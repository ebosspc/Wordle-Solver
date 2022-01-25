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
# Define a function to remove possible words after the first guess
def remove_first_guess_words():
    # Get the first word's data and import it into this module
    word_processing.get_first_word_data()
    word_processing.process_first_word_data()
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

# Remove eliminated words from the possible words list after the first guess
remove_first_guess_words()
print(len(five_letter_words_list))
