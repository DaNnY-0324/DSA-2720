from Lab2_node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def insert_at_position(self, data, position):
        if position < 0 or position > self.length:
            raise ValueError("Invalid position")
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1
    
    def delete_by_value(self, value):
        if not self.head:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            self.length -= 1
            return
        
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            self.length -= 1
    
    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def find_middle(self):
        if not self.head:
            return None
        
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Empty list"