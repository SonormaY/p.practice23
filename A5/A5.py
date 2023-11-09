from validation import Validator
from A5.Collection import Collection
from A5.Strategy import InsertElement, StrategyReadFromFile, StrategyReadFromConsole
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
        print("11. Strategy menu")
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
        elif user_input == "11":
            while True:
                clear()
                print("Strategy menu: ")
                print("1. Add element from file by position")
                print("2. Add element from console")
                print("3. Delete by position")
                print("4. Delete in range")
                print("0. Exit")
                strategy_input = input("Enter number to execute: ")
                strategy = InsertElement()
                if strategy_input == "1":
                    strategy.setStrategy(StrategyReadFromFile())
                    input_file = input("Enter filename: ")
                    while True:
                        try:
                            strategy.executeStrategy(collection, log, input_file, Validator.input_integer("Enter position: "))
                        except FileNotFoundError:
                            print("File does not exist")
                            input("Press enter to continue")
                            break
                        if input("Continue to enter? (y/n): ") != "y": break
                elif strategy_input == "2":
                    strategy.setStrategy(StrategyReadFromConsole())
                    while True:
                        strategy.executeStrategy(collection, log)
                        if input("Continue to enter? (y/n): ") is not "y": break
                elif strategy_input == "3":
                    try:
                        collection.delete_by_index(Validator.input_integer("Enter index to delete: "), log)
                    except IndexError:
                        input("Wrong index, press enter to continue")
                    else:
                        input("Successfully deleted, press enter to continue")
                elif strategy_input == "4":
                    try:
                        collection.delete_in_bounds(
                            Validator.input_integer("Enter start pos: "),
                            Validator.input_integer("Enter end pos: "),
                            log
                            )
                    except ValueError:
                        print("Invalid bounds, press enter to continue")
                    else:
                        input("Successfully deleted, press enter to continue")
                elif strategy_input == "0": break
                else:
                    print("Enter valid number of program")

        elif user_input == "0": break
        else: print("Enter valid number of program")