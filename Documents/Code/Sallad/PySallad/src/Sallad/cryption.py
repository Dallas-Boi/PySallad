# Made 2-28-23 Tuesday

# This file is the encryption and decryption in Sallad

# This will encrypt the Data Given
class cryption:
    global valid_letters
    valid_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){}:\"<>?,./;'[]+_=-\|`~"

    # Constructor

    # Encrypts the given String
    def encrypt(string, forward = None):
        """
        This Encrypts the given String and goes forward in the alphabet the amount of spaces given. If the argument 'forward' is not defined then it will
        set the default to 5.
        """
        # Variables
        new_data = ""
        space = forward
        
        # Error Handling
        if forward == None: space = 5 # Checks if forward was given. If not sets the default to 5
        if type(forward) != int: raise TypeError("forward is not a integer") # Checks if forward does not equal a integer. Raises an error if not

        # This will Encryt the given string and go forward the amount of spaces
        for new in range(len(str(string))):
            for letter in range(len(valid_letters)):
                #print(valid_letters[letter:letter+1])
                # This checks if it needs to start at the beginning
                if str(string)[new:new+1] == valid_letters[letter:letter+1]:
                    #print(f'new: {str(string)[new:new+1]} | letter: {valid_letters[letter+5:letter+6]}')
                    if letter+space < len(valid_letters):
                        # If the list does not have to start at the beginning of "valid_letters"
                        new_data += valid_letters[letter+(space):letter+(space+1)]
                    else:
                        # If the given letter does have to start at the beginning of "valid_letters"
                        index = letter - len(valid_letters)
                        new_data += valid_letters[letter+(space):letter+(space+1)]    
        return new_data+str(space) # This returns the 

    # Decrypts the given String
    def decrypt(string):
        # Variables
        new_data = ""
        give_str = string
        space = 0

        # Error Handler to check if the given string has been encrypted or has a integer at the end
        try:
            space = int(give_str[len(give_str)-1:len(give_str)]) # Sets space to the number at the end of the encrypted string
            give_str = give_str[0:len(give_str)-1] # Removes the number at the end
        except:
            raise TypeError("The given string has not been encrypted before")

        # Decrypts the given string
        for new in range(len(str(give_str))):
            for letter in range(len(valid_letters)):
                #print(valid_letters[letter:letter+1])
                # This checks if it needs to start at the beginning
                if str(give_str)[new:new+1] == valid_letters[letter:letter+1]:
                    #print(f'new: {str(string)[new:new+1]} | letter: {valid_letters[letter-5:letter-4]}')
                    if letter-space < len(valid_letters):
                        # If the list does not have to start at the end of "valid_letters"
                        new_data += valid_letters[letter-space:letter-(space-1)]
                    else:
                        # If the given letter does have to start at the end of "valid_letters"
                        index = len(valid_letters) - letter
                        new_data += valid_letters[index-space:index-(space-1)]   
        return new_data # Returns the decrypted string