#####-Imports-#####
# Import the math library for mathematical functions
import math as math 

# Import random library for random number generation
import random as rand

# Import module that generates the word list 
import word_list_generation as word_list_generation

# Import a module to welcome the user
import welcome as welcome

#####-Setup-#####
# Generate a list of all 5 letter words in English and import it
word_list_generation.get_5_letter_words()
from word_list_generation import five_letter_words_list

#####-User Interface-#####
# Welcome the user to the script
welcome.print_instructions()

# Get the resulting data of what 
word_1_char_1_data = str(input("A: "))
word_1_char_2_data = str(input("A: "))
word_1_char_3_data = str(input("A: "))
word_1_char_4_data = str(input("A: "))
word_1_char_5_data = str(input("A: "))