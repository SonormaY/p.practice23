from A2.A2 import do_some_magic2
from A2.linked_list import LinkedList
if __name__ == "__main__":
    print("Menu: ")
    while True:
        print("№2 LinkedList && ReverseNegativeNumbers")
        user_input = input("Select № of Assignment to execute:")

        if user_input == '2':
            do_some_magic2()
        else: print("Enter valid number")