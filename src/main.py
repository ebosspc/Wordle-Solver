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
# Generate a list of all 5 letter words in English
word_list_generation.get_5_letter_words()
from word_list_generation import five_letter_word_list
print(len(five_letter_word_list))

#####-User Interface-#####

