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

#####-User Interface-#####
# Welcome the user to the script
welcome.print_instructions()

# Get the first word's data and import it into this module
from word_list_generation import five_letter_words_list
word_processing.get_first_word_data()
word_processing.process_first_word_data()
from word_processing import five_letter_words_list
print(len(five_letter_words_list))
