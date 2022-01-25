import main
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

# Define a fucntion to process the received first word data
def process_first_word_data():
    # Create globalized lists that contain the possible letters a specific character in the word can be
    global possible_char_1_list,possible_char_2_list,possible_char_3_list,possible_char_4_list,possible_char_5_list
    possible_char_1_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_2_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_3_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_4_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_5_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_1_data == 'g':
        possible_char_1_list.remove('a')
        possible_char_2_list.remove('a')
        possible_char_3_list.remove('a')
        possible_char_4_list.remove('a')
        possible_char_5_list.remove('a')
    if word_1_char_1_data == 'y':
        possible_char_1_list.remove('a')
    if word_1_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append('a')
    
    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_2_data == 'g':
        possible_char_1_list.remove('d')
        possible_char_2_list.remove('d')
        possible_char_3_list.remove('d')
        possible_char_4_list.remove('d')
        possible_char_5_list.remove('d')
    if word_1_char_2_data == 'y':
        possible_char_2_list.remove('d')
    if word_1_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append('d')

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_3_data == 'g':
        possible_char_1_list.remove('i')
        possible_char_2_list.remove('i')
        possible_char_3_list.remove('i')
        possible_char_4_list.remove('i')
        possible_char_5_list.remove('i')
    if word_1_char_3_data == 'y':
        possible_char_3_list.remove('i')
    if word_1_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append('i')

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_4_data == 'g':
        possible_char_1_list.remove('e')
        possible_char_2_list.remove('e')
        possible_char_3_list.remove('e')
        possible_char_4_list.remove('e')
        possible_char_5_list.remove('e')
    if word_1_char_4_data == 'y':
        possible_char_4_list.remove('e')
    if word_1_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append('e')

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_5_data == 'g':
        possible_char_1_list.remove('u')
        possible_char_2_list.remove('u')
        possible_char_3_list.remove('u')
        possible_char_4_list.remove('u')
        possible_char_5_list.remove('u')
    if word_1_char_5_data == 'y':
        possible_char_5_list.remove('u')
    if word_1_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append('u')
    
    # Remove words based on the new possibilites for character placement
    from main import five_letter_words_list
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
