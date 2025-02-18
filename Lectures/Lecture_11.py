"""
Midterm Exam:
    - February 25, 2024

Topics: (5 Free Response questions)
- Intro to DSA analysis (1 question)
- Stacks & Queues (2 questions)
- Singly Linked List (both linear and circular) (1 question)
- Doubly Linked List (both linear and circular) (1 question)

Cheat Sheet:
- One Sided hand-written 

Circular Linked List:
    Singly:
        - Insertion:
            - At the beginning
            - At the end
            - After a node
        - Deletion:
            - At the beginning
            - At the end
            - After a node
    Doubly:
        - Insertion:
            - At the beginning
            - At the end
            - After a node
        - Deletion:
            - At the beginning
            - At the end
            - After a node
"""

# Implemmentation of Circular Doubly Linked List:

class CDLL:
    def __init__(self):
        self.head = None
    def prepend(self,x):
        p =  Node(x)
        if self.head is None:
            self.head = p
            p.next = self.head    
            p.prev = p
        else:
            p.next = self.head
            p.prev = self.head.prev
            self.head.prev = p
            p.prev.next = p
            self.head = p        

    def append(self,x):
        p = Node(x)
        if self.head is None:
            self.head = p
            p.next = self.head
            p.prev = p
        else:
            p.next = self.head
            p.prev = self.head.prev
            self.head.prev.next = p
            self.head.prev = p

    def deletef(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is self.head:
            self.head = None
            return
        else:
            p = self.head
            self.head = p.next
            self.head.prev = p.prev
            p.prev.next = self.head
            p.prev = None
            p.next = None


class Node:
    def __init__(self,data):
        self.info = data
        self.prev = None    
        self.next = None

# main script
cdll = CDLL()
cdll.prepend(10)
cdll.prepend(20)
cdll.prepend(30)
cdll.append(40)
cdll.deletef()