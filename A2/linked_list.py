from node import Node
import random

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
 
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
 
        current_node.next = new_node
    def insertAtIndex(self, data, index):
        if index < 0: raise Exception("Enter valid index")
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node and position+1 != index):
                position += 1
                current_node = current_node.next
 
            if current_node:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                raise Exception("Index is not present")

    def writeAtIndex(self, data, index):
        if index < 0: raise Exception("Enter valid index")
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = data
        else:
            while(current_node and position != index):
                position += 1
                current_node = current_node.next
 
            if current_node:
                current_node.data = data
            else:
                raise Exception("Index is not present")
    
    def deleteAtStart(self):
        if self.head is None:
            return
        
        self.head = self.head.next
    def deleteAtEnd(self):
        if self.head is None:
            return
        
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next

        current_node.next = None
    def deleteAtindex(self, index):
        if index < 0: raise Exception("Enter valid index")
        if self.head is None:
            return
        
        current_node = self.head
        position = 0
        if position == index:
            self.deleteAtStart()
        else:
            while(current_node and position+1 != index):
                position += 1
                current_node = current_node.next

            if current_node:
                current_node.next = current_node.next.next
            else:
                raise Exception("Index is not present")          
    def deleteByData(self, data):
        current_node = self.head
 
        while(current_node and current_node.next.data != data):
            current_node = current_node.next
 
        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next
    
    def size(self):
        size = 0
        if self.head :
            current_node = self.head
            while current_node:
                size = size + 1
                current_node = current_node.next
                return size
            else:
                return 0    
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next   
    def swap(self, index1, index2):
        if index1 == index2:
            return
        
        prev1, curr1 = None, self.head
        prev2, curr2 = None, self.head
        pos1, pos2 = 0, 0

        while curr1 and pos1 != index1:
            prev1 = curr1
            curr1 = curr1.next
            pos1 += 1

        while curr2 and pos2 != index2:
            prev2 = curr2
            curr2 = curr2.next
            pos2 += 1
        
        if pos1 != index1 or pos2 != index2 or (curr1 is None and curr2 is None):
            raise Exception("Invalid indices")
        
        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next


    def input(self):
        print("Type 'stop' to stop input process")
        while True:
            data = input("Enter data: ")
            if data == "stop": 
                break

            self.insertAtEnd(data)
    def randomFill(self, amount, a, b):
        if amount < 1: raise Exception("Enter valid amount")
        if a > b: raise Exception("Wrong bounds of random generation")
        for i in range (0, amount):
            self.insertAtEnd(random.randint(a, b))

