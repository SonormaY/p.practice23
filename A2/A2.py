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
            choice = input("Enter 1 to input list manually or 2 to generate randomly. Enter 'e' to exit: ")
            if choice == '1':
                ll.input()
                break
            elif choice == '2':
                a = input("Enter a: ")
                b = input("Enter b: ")
                amount = input("Enter amount to generate: ")
                if validate_int(a) and validate_int(b) and validate_positive_int(amount):
                    ll.randomFill(int(amount), int(a), int(b))
                    print("LinkedList:")
                    ll.print()
                else: print("Error in input data!!!")
                break
            elif choice == 'e':
                return
            else: print("Enter a valid number")
        ll.reverseNegativeNumbers()
        print()
        ll.print()
