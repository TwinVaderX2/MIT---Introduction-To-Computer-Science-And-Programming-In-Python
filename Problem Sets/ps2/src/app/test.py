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
    my_word_length = len(my_word.strip(" "))
    other_word_length = len(other_word)

    print(my_word_length, other_word_length)

my_word = "a_ _ pl_"
other_word = "apple"

match_with_gaps(my_word,other_word)