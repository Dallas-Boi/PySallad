# Made 4-25-23 Tuesday

# This script converts different currency / measurements / etc. to somethine else

# Converts Currency
def convert_measurement(amount = 1, convert_type = None, convert_from = None, convert_to = None):

    # Checks if the given Arg* are valid 
    if type(amount) != int: raise TypeError("The arg* 'amount' must be a Integer"); # amount is not a String

    if convert_type == None: raise ValueError("The arg* 'convert_type' must equal a value"); # convert_type is not given
    if type(convert_type) != str: raise TypeError("The arg* 'convert_type' must be a string"); # convert_type is not a String

    if convert_from == None: raise ValueError("The arg* 'convert_from' must equal a value"); # convert_from is not given
    if type(convert_from) != str: raise TypeError("The arg* 'convert_from' must be a string"); # convert_from is not a String

    if convert_to == None: raise ValueError("The arg* 'convert_to' must equal a value"); # convert_to is not given
    if type(convert_to) != str: raise TypeError("The arg* 'convert_to' must be a string"); # convert_to is not a String

    # Checks the Type
    if convert_type.lower() == "length": # If the convert_type is length

        measureArray = {
            "nanometer": { 
                "divide": [1000, 1e-6, 1e-7, 1e-9, 1e-12],
                "multiply": [1]
            },

        }

        mathType = ""
        value = 1

        if convert_from.lower() == "nanometer": # If convert_from is "nanometer"
            print()
