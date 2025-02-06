class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, x):
        new_node = Node(x)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow: Cannot dequeue from an empty queue.")
            return "Queue is empty"
        
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Test cases for Queue using Singly Linked List
queue_ll = QueueLinkedList()
print("Enqueueing elements: 10, 20, 30")
queue_ll.enqueue(10)
queue_ll.enqueue(20)
queue_ll.enqueue(30)
queue_ll.display()

print("Dequeued:", queue_ll.dequeue())  # Should print 10
queue_ll.display()

print("Dequeued:", queue_ll.dequeue())  # Should print 20
print("Dequeued:", queue_ll.dequeue())  # Should print 30
print("Dequeued:", queue_ll.dequeue())  # Queue underflow case

queue_ll.display()  # Should indicate queue is empty
