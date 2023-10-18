# Problem Set 4C
# Name: Phillip van Staden
# Collaborators:

import random
import string
from ps4a import get_permutations
from ps4b import load_words,words_full_path,is_word
import os

### HELPER CODE ###
# removed helper code and imported from ps4b
### END HELPER CODE ###

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

class SubMessage():
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(words_full_path)

    def __str__(self):
        '''
        Method used to display/print message_text in terminal

        returns string
        '''
        return f'The original message is: {self.message_text}'
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        valid_words_copy = self.valid_words.copy()

        return valid_words_copy
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        

        # LOWER CASE
        # create list of vowels
        lower_vowels_ls = [i for i in VOWELS_LOWER]
        # create dictionary with key (vowel) + item (vowels_permutation)
        lower_vowels_dict = dict(zip(lower_vowels_ls,vowels_permutation))
        # create list of consonants
        lower_consonants_ls = [i for i in CONSONANTS_LOWER]
        # create dictionary of consonants with key = item
        lower_consonants_dict = dict(zip(lower_consonants_ls,lower_consonants_ls))
        # join two dictionaries
        lower_dict = {**lower_vowels_dict,**lower_consonants_dict}

        # UPPER CASE
        # repeat lower case for upper case
        upper_vowels_ls = [i for i in VOWELS_UPPER]
        upper_vowels_dict = dict(zip(upper_vowels_ls,[x.upper() for x in vowels_permutation]))
        upper_consonants_ls = [i for i in CONSONANTS_UPPER]
        upper_consonants_dict = dict(zip(upper_consonants_ls,upper_consonants_ls))
        upper_dict = {**upper_vowels_dict,**upper_consonants_dict}

        cipher = {**lower_dict,**upper_dict}

        return cipher

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        # self.message_text = 'Hello World!'
        
        new_message = ''
        # create list of char in message
        message_ls = [i for i in self.message_text]
        # iterate through list
        for idx in message_ls:
            if idx.lower() in alphabet:
                new_message = new_message + transpose_dict.get(idx)
            else:
                new_message = new_message + idx

        return new_message
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(words_full_path)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message
        
        Hint: use your function from Part 4A
        '''
        # get permutations of vowels
        permutations_ls = get_permutations(VOWELS_LOWER)
        # create permutations_dict with item = 0
        permutations_dict = dict.fromkeys(permutations_ls,0)
        
        def decrypt_message(transpose_dict,message):
            # create list of letters in message
            message_ls = [i for i in message]
            # create new_message variable
            new_message = ''
            # iterate through list
            for letter in message_ls:
                if letter.lower() in alphabet:
                    new_message = new_message + transpose_dict.get(letter)
                else:
                    new_message = new_message + letter
            
            return new_message

        # iterate through each permutation
        for perm in permutations_ls:
            count = 0
            # build transpose_dict
            transpose_dict = self.build_transpose_dict(perm)
            # decrypt message
            decrypted_message = decrypt_message(transpose_dict,self.message_text)
            # create list of words
            decrypted_message_ls = decrypted_message.strip('!.?,').split(' ')
            # test each word if valid
            for word in decrypted_message_ls:
                # count number of valid words
                if word.lower() in self.valid_words:
                    count += 1
            # update permutations_dict with word count
            permutations_dict[perm] = count
        
        # return list of permutations with max word count
        max_keys = [key for key, value in permutations_dict.items() if value == max(permutations_dict.values())]
        
        # select random permution from list and return tuple with permutation,decrypted message
        # choose random element from list
        random_permutation = random.choice(max_keys)
        # build tuple that displays the shift_key and decrypted message
        best_cipher = (random_permutation,decrypt_message(self.build_transpose_dict(random_permutation),self.message_text))
        
        return best_cipher
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
