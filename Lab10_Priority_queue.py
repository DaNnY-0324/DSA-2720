class PriorityQueue:
    def __init__(self):

        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty priority queue")
        return self.heap[0]

    def extract(self):
        if self.is_empty():
            raise IndexError("Extract from empty priority queue")
        min_item = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._heapify_down(0)
        return min_item

    def is_empty(self):
        return len(self.heap) == 0

    def length(self):
        return len(self.heap)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self.heap)

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
