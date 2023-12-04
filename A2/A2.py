from A2.linked_list import LinkedList

def validate_positive_int(n):
    return n.isdigit() and int(n) > 0

def validate_int(n):
    if n[0] == '-':
        return n[1:].isdigit()
    return n.isdigit()

def do_some_magic2():
    while exit:
        ll = LinkedList()
        while True:
            print("Menu: ")
            print("1. Manual input")
            print("2. Random input")
            print("3. Add element to k index")
            print("4. Delete element at k index")
            print("5. Reverse negative numbers")
            print("6. Print LL")
            print("7. Clear LL")
            choice = input("Enter number: ")
            if choice == '1':
                ll.input()
                input("Press Enter to continue...")
            elif choice == '2':
                n = input("Input number of elements to generate")
                a = input("Input a")
                b = input("Input b")
                if validate_positive_int(n) and validate_int(a) and validate_int(b):
                    ll.randomFill(n, a, b)
                input("Press Enter to continue...")
            elif choice == '3':
                i = input("Enter index: ")
                if validate_positive_int(i):
                    ll.insertAtIndex(i, int(input("Enter data: ")))
                input("Press Enter to continue...")
            elif choice == '4':
                i = input("Enter index: ")
                if validate_positive_int(i):
                    ll.deleteAtindex(int(i))
                input("Press Enter to continue...")
            elif choice == '5':
                ll.reverseNegativeNumbers()
                input("Press Enter to continue...")
            elif choice == '6':
                ll.print()
                input("Press Enter to continue...")
            elif choice == '7':
                ll.clear()
                input("Press Enter to continue...")
            elif choice == '0':
                exit
            else: print("Enter a valid number")