class QueueList:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow: The queue is empty")
            return None
        return self.queue.pop(0)
    
    def display(self):
        print("Queue:", self.queue)


# Test cases for Queue using Python List
queue_list = QueueList()
queue_list.enqueue(10)
queue_list.enqueue(20)
queue_list.enqueue(30)
queue_list.display()
print("Dequeued:", queue_list.dequeue())
queue_list.display()
print("Dequeued:", queue_list.dequeue())
print("Dequeued:", queue_list.dequeue())
print("Dequeued:", queue_list.dequeue())

    
