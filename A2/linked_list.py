from node import Node

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
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                raise Exception("Index is not present")

    def writeAtIndex(self, data, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = data
        else:
            while(current_node and position != index):
                position = position+1
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
        if self.head is None:
            return
        
        current_node = self.head
        position = 0
        if position == index:
            self.deleteAtStart()
        else:
            while(current_node and position+1 != index):
                position = position + 1
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