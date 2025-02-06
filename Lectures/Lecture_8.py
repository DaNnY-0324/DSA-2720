# Counting Amount Of Nodes
def count(self):
    cnt = 0
    if self.head is None:
        print(cnt)
    else:
        cnt += 1
        p = self.head
        while p is not None:
            p = p.next
            cnt += 1
        print(cnt)

# Deleting First Node
def deletef(self):
    if self.head is None: 
        return
    if self.head.next is None:
        self.head = None
        return
    p =  self.head
    self.head = self.head.next
    self.head.prev = None
    p.next = None
    p = None

# Deleting Last Node
def deletel(self):   
    if self.head is None: 
        return
    if self.head.next is None:
        self.head = None
        return
    q = self.head
    p = q.next
    while p.next is not None:
        p = p.next
        q = q.next
    q.next = None
    p.prev = None 
    p = None

# Print The List In Reverse Order
# Recursive Method: Function Calling Itself
def fun(self):
    if self is not None:
        fun(self.head.next)
        print(self.head.info)

