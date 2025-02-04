class Node: 
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    """Stack implementation using a singly linked list."""
    def __init__(self):
        self.top = None

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None  # Return True if top is None

    def push(self, data):
        """Pushes an element onto the stack."""
        new_node =Node(data) 
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Removes and returnbs the top element of the stack. Checks for underflow.""" 
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack")
        popped_data =self.top.data
        self.top = self.top.next
        return popped_data
    
    def peek(self): 
        """Returns the top element of the stack without removing it from the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty: Cannot peek at an empty stack")
        return self.top.data
    
# Test cases
if __name__ == "__main__":
    stack = StackLinkedList()

    # Test pushing elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    # Test peeking
    print("Top element:", stack.peek())  # Output: 30

    # Test popping elements
    print("Popped:", stack.pop())  # Output: 30
    print("Popped:", stack.pop())  # Output: 20

    # Test underflow
    stack.pop()  # Removing last element (10)
    try:
        stack.pop()  # Should raise an IndexError
    except IndexError as e:
        print(e)  # Output: Stack Underflow: Cannot pop from an empty stack
