class StackList:
    """Stack implementation using Python lists."""
    
    def __init__(self):
        self.stack = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def push(self, data):
        """Pushes an element onto the stack."""
        self.stack.append(data)

    def pop(self):
        """Removes and returns the top element of the stack. Checks for underflow."""
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """Returns the top element of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty: Cannot peek at an empty stack")
        return self.stack[-1]

    def __str__(self):
        """Returns a string representation of the stack (top to bottom)."""
        return "Stack (top → bottom): " + " -> ".join(map(str, reversed(self.stack)))

# Test Cases
if __name__ == "__main__":
    stack = StackList()

    # Test pushing elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print(stack)  # Expected Output: Stack (top → bottom): 30 -> 20 -> 10
    
    # Test peeking
    print("Top element:", stack.peek())  # Output: 30

    # Test popping elements
    print("Popped:", stack.pop())  # Output: 30
    print(stack)  # Updated stack: Stack (top → bottom): 20 -> 10
    
    print("Popped:", stack.pop())  # Output: 20
    print(stack)  # Updated stack: Stack (top → bottom): 10

    print("Popped:", stack.pop())  # Output: 10
    print(stack)  # Updated stack: Stack (top → bottom):

    # Test underflow with try-except
    try:
        print("Popped:", stack.pop())  # This should trigger an underflow error
    except IndexError as e:
        print("Error:", e)  # Output: Stack Underflow: Cannot pop from an empty stack
