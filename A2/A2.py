from A2.linked_list import LinkedList

def do_some_magic2():
    ll = LinkedList()
    choice = int(input("Enter 1 to input list manually or 2 to generate randomly: "))
    if choice == 1:
        ll.input()
    elif choice == 2:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        amount = int(input("Enter amount to generate: "))
        ll.randomFill(amount, a, b)
        print("LinkedList:")
        ll.print()
    ll.reverseNegativeNumbers()
    print()
    ll.print()