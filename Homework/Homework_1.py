#Instructions

"""1. Suppose an initially empty stack S has executed 25 push operations, 12 top
operations, and 10 pop operations, 3 of which raised Empty errors that were
caught and ignored. What is the current size of S?"""

# Answer: 18 

"""2. What values are returned during the following stack operations, if executed
upon an empty stack? push(5), push(3), pop(), push(2),
push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(), pop(),
push(4), pop(), pop()."""

# Answer: 3, 8, 2, 1, 6, 7, 4, 9

"""3. What values are returned during the following sequence of queue
operations, if executed on an initially empty queue? enqueue(5),
enqueue(3), dequeue(), enqueue(2), enqueue(8), dequeue(), dequeue(),
enqueue(9), enqueue(1), dequeue(), enqueue(7), enqueue(6), dequeue(),
dequeue(), enqueue(4), dequeue(), dequeue()."""

# Answer: 5, 3, 2, 8, 9, 1, 7, 6

"""4. Suppose an initially empty queue Q has executed 32 enqueue operations, 10
first operations, and 15 dequeue operations, 5 of which raised Empty errors
that were caught and ignored. What is the current size of Q?"""

# Answer: 22

"""5. Consider the following Python function:

def g(list1, list2):
    p = list1
    while p.next:
        p = p.next
    p.next = list2

Assuming that list1 and list2 point to valid None-terminated linked lists, what
will be the result of calling the given function g?"""

# Answer: The function will append list2 to the end of list1.

"""6. The following Python function takes a singly linked list of integers as a
parameter and rearranges the elements of the list. The function is called with
the list containing the integers 11, 22, 33, 44, 55 in the given order. What will be
the contents of the list after the function completes execution?

def rearrange(list_head):
    if not list_head or not list_head.next:
        return
    p = list_head
    q = list_head.next
    while q:
        temp = p.value
        p.value = q.value
        q.value = temp
        p = q.next
        q = p.next if p else None
"""

# Answwer: The list is modified to [22, 11, 44, 33, 55] by swapping adjacent values.
