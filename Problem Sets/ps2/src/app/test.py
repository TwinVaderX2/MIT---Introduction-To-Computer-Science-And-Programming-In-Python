def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # set variables
    is_match = False
    my_word_length = 0
    other_word_length = len(other_word)
    my_word_list = []
    other_word_list = []

    # split my_word into characters in list
    for idx in my_word:
        if idx != " ":
            my_word_list.append(idx.strip())

    # set length of my_word_length
    my_word_length = len(my_word_list)

    # split other_word into characters in list
    for idx in other_word:
        other_word_list.append(idx)

    # test if lenghts of two words are match
    if my_word_length == other_word_length:
        # test characters in each position of both words for match
        # set is_match to TRUE if positions match
        for idx in range(other_word_length):
            if my_word_list[idx] == other_word_list[idx] or my_word_list[idx] == "_":
                is_match = True
            # if match not found return false and break loop
            else:
                is_match = False
                break
    
    return is_match

my_word = "st_ _ t"
other_word = "tout"

print(match_with_gaps(my_word,other_word))