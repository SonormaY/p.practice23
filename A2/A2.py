from A2.linked_list import LinkedList

def do_some_magic2():
    ll = LinkedList()
    choice = input("Enter 1 to input list manually or 2 to generate randomly: ")
    while True:
        if choice == '1':
            ll.input()
            break
        elif choice == '2':
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            amount = int(input("Enter amount to generate: "))
            ll.randomFill(amount, a, b)
            print("LinkedList:")
            ll.print()
            break
        else: print("Enter a valid number")
    ll.reverseNegativeNumbers()
    print()
    ll.print()