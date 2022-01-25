# Define a function to collect the corresponding data for the first word entered
def get_first_word_data():
    # Globalize data variables that will be used in other modules
    global word_1_char_1_data,word_1_char_2_data,word_1_char_3_data,word_1_char_4_data,word_1_char_5_data

    # Get the resulting data of the first word's first character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_1_data = str(input("A: "))
        if word_1_char_1_data == 'g' or word_1_char_1_data == 'y' or word_1_char_1_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's second character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_2_data = str(input("D: "))
        if word_1_char_2_data == 'g' or word_1_char_2_data == 'y' or word_1_char_2_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's third character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_3_data = str(input("I: "))
        if word_1_char_3_data == 'g' or word_1_char_3_data == 'y' or word_1_char_3_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's fourth character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_4_data = str(input("E: "))
        if word_1_char_4_data == 'g' or word_1_char_4_data == 'y' or word_1_char_4_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's fifth character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_5_data = str(input("U: "))
        if word_1_char_5_data == 'g' or word_1_char_5_data == 'y' or word_1_char_5_data == 'gr':
            continue_with_loop = 1