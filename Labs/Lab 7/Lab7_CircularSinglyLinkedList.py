class Node:
    """
    Represents a node in the circular singly linked list.
    """
    def __init__(self, data):
        """
        Constructor for the Node class.
        
        Parameters:
            data (any type): The value stored in the node.
            
        Attributes:
            self.data: Stores the node's data.
            self.next: Points to the next node (initially None).
        """
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    """
    Implements a circular singly linked list.
    """
    def __init__(self):
        """
        Constructor for the CircularSinglyLinkedList class.
        
        Parameters: None
        
        Attributes:
            self.head: Stores the reference to the first node in the list (initially None).
        """
        self.head = None
    
    def insert_first(self, data):
        """
        Inserts a new node at the beginning of the list.
        
        Parameters:
            data (any type): The value to be inserted.
            
        Return Type: None
        """
        # Create a new node
        new_node = Node(data)
        
        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = new_node  # Point to itself to form a circle
        else:
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            
            # Update connections
            new_node.next = self.head
            self.head = new_node
            current.next = self.head
    
    def insert_last(self, data):
        """
        Inserts a new node at the end of the list.
        
        Parameters:
            data (any type): The value to be inserted.
            
        Return Type: None
        """
        # Create a new node
        new_node = Node(data)
        
        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = new_node  # Point to itself to form a circle
        else:
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            
            # Update connections
            current.next = new_node
            new_node.next = self.head
    
    def delete_first(self):
        """
        Deletes the first node in the list.
        
        Parameters: None
        
        Return Type: None
        """
        # If list is empty
        if self.head is None:
            return
        
        # If only one node in the list
        if self.head.next == self.head:
            self.head = None
            return
        
        # Find the last node
        current = self.head
        while current.next != self.head:
            current = current.next
        
        # Update connections
        current.next = self.head.next
        self.head = self.head.next
    
    def delete_last(self):
        """
        Deletes the last node in the list.
        
        Parameters: None
        
        Return Type: None
        """
        # If list is empty
        if self.head is None:
            return
        
        # If only one node in the list
        if self.head.next == self.head:
            self.head = None
            return
        
        # Find the second to last node
        current = self.head
        while current.next.next != self.head:
            current = current.next
        
        # Update connections
        current.next = self.head
    
    def display(self):
        """
        Displays all elements in the list.
        
        Parameters: None
        
        Return Type: None
        """
        # If list is empty
        if self.head is None:
            print("List is empty")
            return
        
        # Traverse and print each node
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")
    
    def search(self, data):
        """
        Searches for a node with the given data.
        
        Parameters:
            data (any type): The value to search for.
            
        Return Type: Boolean (True if found, False otherwise)
        """
        # If list is empty
        if self.head is None:
            return False
        
        # Traverse and check each node
        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        
        return False