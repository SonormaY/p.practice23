from os import system, name
from validation import Validator
from A4.A4 import do_some_magic4

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


while True:
    clear()
    while True:
        user_input = input("Enter number to execute (enter 0 to exit): ")
        if Validator.is_integer(user_input):
            break
        else: print("Enter a number")
    if user_input == "4":
        do_some_magic4()
        print()
        input("Press enter to continue...")
    elif user_input == "0": break
    else: 
        print("Enter valid number of program")
        input("Press enter to continue...")