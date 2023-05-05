# Made 4-21-23 Friday

# This file is made to sort a list or array list (JSON) from A-z or 0-9

def sortList(sList):
    # This will check for error / if "list" is not a list type
    if type(sList) != list: raise TypeError("The given argument is not a list")

    returnedList = []
    mylist = ["1world", "LearnPython.com", "pineapple", "bicycle", "Word"]
    sorted_list = sorted(mylist)
    print(sorted_list)

sortList(["hi"])