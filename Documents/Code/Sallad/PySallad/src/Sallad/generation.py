# Made 2-28-23 Tuesday

# This file encrypts, decrypts, generates IDs, and Generates Seeds items
# The encryption works by taking the list of the valid letters, finding the current letter of the given String, 
# then getting the letter 5 places infront of the current String

# Imports
import random
import time
    
# This class can generate Seeds (WIP) and IDs
class Generate:
    global valid_letters, valid_numbers, valid_symbols
    valid_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valid_numbers = "1234567890"
    valid_symbols = "!@#$%^&*(){}:\"<>?,./;'[]+_=-\|`~"

    # Generates an ID with the given "ud_length"
    def generate_id(id_length, has_letters=False, has_numbers=False, has_symbols=False):

        # Checks if the letters are booleans
        if type(has_letters) is not bool: raise TypeError(f'"{has_letters}" is not a boolean'); # Raise a error if "has_letters" is not a boolean
        if type(has_numbers) is not bool: raise TypeError(f'"{has_numbers}" is not a boolean'); # Raise a error if "has_numbers" is not a boolean
        if type(has_symbols) is not bool: raise TypeError(f'"{has_symbols}" is not a boolean'); # Raise a error if "has_symbols" is not a boolean
        
        # Checks if all of the parameters are false | If they are all false it enables "has_letters"
        if (bool(has_letters) == False) and (bool(has_numbers) == False) and (bool(has_symbols) == False): has_letters = True;
        
        # This combines all the given items into one
        valid_items = ""
        if has_letters == True: valid_items += valid_letters;
        if has_numbers == True: valid_items += valid_numbers;
        if has_symbols == True: valid_items += valid_symbols;

        # This makes the Id
        output = ""
        while True:
            # Generates a random number
            random_number = random.randint(0, len(valid_items)-1)
            # Adds the random selected number to the output
            output += valid_items[random_number:random_number+1]

            # Checks if the length of the output is equaled to "id_length"
            if len(output) == id_length: break;

        # Returns the generated ID
        return output
        

#print(str(time.ctime(time.time())))