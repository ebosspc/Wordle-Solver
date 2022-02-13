# Define a function to generate a list of 5 letter words
def get_5_letter_words_list():
    # Create a list to store 5 letter words
    global five_letter_words_list
    five_letter_words_list = []

    # Open the word database and add 5 letter words to a corresponding list
    words_database_file = open("Words_English.txt", 'r')
    for line in words_database_file:
        individual_word = line.strip() # Remove the endline character from each line before storing
        if len(individual_word) == 5:
            five_letter_words_list.append(individual_word) # Break up word into list of characters
