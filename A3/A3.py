from os import system, name
from valiation import Validator
from A3.linked_list import LinkedList
import random

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def do_some_magic3():
    clear()
    ll = LinkedList()
    for i in range(10):
        ll.insertAtEnd(random.randint(1, 10))
    print(f"Randomly generated Linked list: {ll}")
    print()

    ll_iter = iter(ll)
    try:
        while True:
            print(f"Current iteration: {next(ll_iter)}")
    except StopIteration:
        print("Iteration stopped")
    print()
    
    ll.clear()
    for i in range(10):
        ll.insertAtEnd(random.randint(1, 10))
    print(f"Randomly generated Linked list: {ll}", " ")
    print()

    ll_iter = iter(ll)
    gen = LinkedList.generator(ll)
    try:
        while True:
            print(f"Current iteration: {next(gen)}")
    except StopIteration:
        print("Iteration stopped")
    