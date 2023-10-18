from validation import Validator
from A4.Collection import Collection
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def do_some_magic4():
    collection = Collection()
    clear()
    log = "out"
    while True:
        clear()
        print("Menu: ")
        print("1. Print Requests")
        print("2. Clear Requests")
        print("3. Add element manually")
        print("4. Read Requests from file")
        print("5. Find Request by ID")
        print("6. Sort Requests by type")
        print("7. Delete Request by ID")
        print("8. Edit Request by ID")
        print("9. Write log file name")
        print("10. Print log")
        print("0. Exit")
        print(f"Log file: {log}")
        while True:
            user_input = input("Enter number to execute: ")
            if Validator.is_integer(user_input):
                break
            else: print("Enter a number")
        if user_input == "1":
            clear()
            collection.print()
            input("Press Enter to continue")
        elif user_input == "2":
            clear()
            collection.clear(log)
            input("Press Enter to continue")
        elif user_input == "3":
            clear()
            collection.add_element_console(log)
            input("Press Enter to continue")
        elif user_input == "4":
            clear()
            try:
                collection.read_from_file(
                    input("Input filename to read from: "),
                    log
                )
            except FileNotFoundError as e:
                print(e)
            input("Press Enter to continue")
        elif user_input == "5":
            clear()
            temp = collection.find_elements(input("Enter value to search: "))
            for request in temp:
                print(request)
            input("Press Enter to continue")
        elif user_input == "6":
            clear()
            collection.sort_data(input("Enter Sort Type: ID/patient_name/patient_phone/vaccine/date/start_time/end_time: "))
            input("Press Enter to continue")
        elif user_input == "7":
            clear()
            collection.delete_by_id(
                input("Enter ID to delete: "),
                log
            )
            input("Press Enter to continue")
        elif user_input == "8":
            clear()
            collection.edit_by_id(
                input("Enter ID to edit: "),
                input("Enter Type: ID/patient_name/patient_phone/vaccine/date/start_time/end_time: "),
                input("Enter value to write: "), 
                log
            )
            input("Press Enter to continue")
        elif user_input == "9":
            clear()
            log = input("Enter log file name: ")
            input("Press Enter to continue")
        elif user_input == "10":
            clear()
            try:
                Collection.print_log(log)
            except FileNotFoundError as e:
                print(e)
            input("Press Enter to continue")
        elif user_input == "0": break
        else: print("Enter valid number of program")