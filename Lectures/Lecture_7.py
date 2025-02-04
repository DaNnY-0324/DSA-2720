# Doubly Linked List Implementation

# main script

class DoublyLinkedList:
    def __init__(self):
        self.head = None

def insertf(self, x):
    p = Node(x)
    if self.head is None:
        self.head = p
    else:
        p.next = self.head
        self.head.prev = p 
        self.head = p 

def inserte(self,x):
    p = Node(x)
    if self.head is None:
        self.head = p
    else:
        q = self.head
        while q.next is not None:
            q = q.next
        p.prev = q
        q.next= p

def display(self):
    if self.head is not None:
        q = self.head
        while q is not None:
            print(q.info)
            q = q.next

class Node:
    def __init__(self, data):
        self.info = data
        self.prev = None
        self.next = None

dll = DoublyLinkedList()
dll.insertf(10)
dll.insertf(20)
dll.insertf(15)
dll.inserte(30)
dll.display()