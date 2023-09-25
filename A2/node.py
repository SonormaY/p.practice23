class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        if type(node) == type(Node(None)):
            self.next = node
    def __str__(self):
        return str(self.val)

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None