"""
1. An airport is developing a computer simulation of air-traffic control that handles events
such as landings and takeoffs. Each event has a time stamp that denotes the time when
the event will occur. The simulation program needs to efficiently perform the following
two fundamental operations:

a. Insert an event with a given time stamp (that is, add a future event).
Answer:
Use a min-heap to insert the event with O(log n) efficiency.

b. Extract the event with smallest time stamp (that is, determine the next event to
process).
Answer:
Use a min-heap to extract the minimum time-stamped event with O(log n) efficiency.

Which data structure should be used for the above operations? Why?
Answer:
A **min-heap (priority queue)** should be used. This data structure efficiently supports:
- Insertion in O(log n)
- Access and removal of the smallest element in O(log n)
The root of a min-heap is always the event with the smallest time stamp, which makes it ideal for simulating time-based events like landings and takeoffs.
"""

"""
2. Bill claims that a preorder traversal of a heap will list its keys in nondecreasing order. Draw
an example of a heap that proves him wrong.
Answer:
Example of a min-heap:

        2
       / \
      4   3

Preorder traversal: 2, 4, 3  
Expected sorted order: 2, 3, 4  
→ This proves Bill is wrong because preorder is NOT guaranteed to be sorted.
"""

"""
3. Hillary claims that a postorder traversal of a heap will list its keys in nonincreasing order.
Draw an example of a heap that proves her wrong.
Answer:
Example of a min-heap:

        1
       / \
      2   3

Postorder traversal: 2, 3, 1  
Expected reverse sorted order: 3, 2, 1  
→ This proves Hillary is wrong because postorder is NOT guaranteed to be reverse sorted.
"""
