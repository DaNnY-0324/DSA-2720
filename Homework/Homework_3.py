"""
Instructions: Please complete the following questions on a separate sheet of paper. After you have
finished, scan your work and upload it to Homework Assignment 3 in our Gradescope for the CSC 2720
DATA STRUCTURES XLS Group ACS11 Spring Semester 2025 course.
"""

"""
1. Suppose that x and y are references to nodes of circularly linked lists, although not necessarily the
same list. Describe a fast algorithm for telling if x and y belong to the same list.

Answer:
To determine if nodes x and y belong to the same circularly linked list:

1. Start from node x and follow the next pointers
2. If we encounter node y before returning to x, then x and y belong to the same list
3. If we return to x without encountering y, then they belong to different lists

Pseudocode:
function sameCircularList(x, y):
    if x == y:
        return true
    
    current = x.next
    while current != x and current != null:
        if current == y:
            return true
        current = current.next
    
    return false

This algorithm has O(n) time complexity, where n is the length of the list containing x.
"""

"""
2. Describe in detail how to swap two nodes x and y (and not just their contents) in a singly linked
list L given references only to x and y. Repeat this exercise for the case when L is a doubly linked
list. Which algorithm takes more time?

Answer:
For a Singly Linked List:

Swapping nodes x and y with references only to x and y requires finding their predecessors:

Pseudocode:
function swapNodes(L, x, y):
    // If x and y are the same, no swap needed
    if x == y:
        return
        
    // Initialize pointers
    prevX = null
    currX = L.head
    prevY = null
    currY = L.head
    
    // Find x and its predecessor
    while currX != null and currX != x:
        prevX = currX
        currX = currX.next
        
    // Find y and its predecessor
    while currY != null and currY != y:
        prevY = currY
        currY = currY.next
    
    // If either x or y is not in the list
    if currX == null or currY == null:
        return
        
    // If x is not the head, update prevX.next
    if prevX != null:
        prevX.next = currY
    else:
        L.head = currY
        
    // If y is not the head, update prevY.next
    if prevY != null:
        prevY.next = currX
    else:
        L.head = currX
        
    // Swap the next pointers
    temp = currX.next
    currX.next = currY.next
    currY.next = temp

Special cases to handle:
- If x and y are adjacent (e.g., prevY == x), adjust the pointers accordingly
- If x or y is the head of the list

For a Doubly Linked List:

function swapNodesDoubly(L, x, y):
    // If x and y are the same, no swap needed
    if x == y:
        return
    
    // Update next pointers
    xNext = x.next
    yNext = y.next
    
    // Handle adjacency cases
    if x.next == y:  // x is directly before y
        x.next = yNext
        y.next = x
        
        if yNext != null:
            yNext.prev = x
            
        y.prev = x.prev
        x.prev = y
        
        if y.prev != null:
            y.prev.next = y
        else:
            L.head = y
    
    elif y.next == x:  // y is directly before x
        y.next = xNext
        x.next = y
        
        if xNext != null:
            xNext.prev = y
            
        x.prev = y.prev
        y.prev = x
        
        if x.prev != null:
            x.prev.next = x
        else:
            L.head = x
    
    else:  // x and y are not adjacent
        x.next = yNext
        y.next = xNext
        
        if xNext != null:
            xNext.prev = y
            
        if yNext != null:
            yNext.prev = x
            
        // Swap prev pointers
        xPrev = x.prev
        yPrev = y.prev
        
        x.prev = yPrev
        y.prev = xPrev
        
        if xPrev != null:
            xPrev.next = y
        else:
            L.head = y
            
        if yPrev != null:
            yPrev.next = x
        else:
            L.head = x

Time Comparison:
The singly linked list algorithm takes O(n) time because we need to locate the predecessors of both nodes, which may require traversing the entire list.

The doubly linked list algorithm takes O(1) time because we have direct access to the nodes' predecessors through their prev pointers.

Therefore, the singly linked list algorithm takes more time.
"""

"""
3. Describe, in pseudo-code, an algorithm for computing the number of descendants of each node of
a binary tree. The algorithm should be based on the Euler tour traversal.

Answer:
For an Euler tour traversal to count descendants:

function countDescendants(root):
    time = 0
    entryTime = {}  // Map of node to entry time
    exitTime = {}   // Map of node to exit time
    
    // Perform Euler tour
    eulerTour(root, entryTime, exitTime, time)
    
    descendants = {}  // Map of node to descendant count
    
    // Calculate descendants for each node
    for each node in tree:
        descendants[node] = (exitTime[node] - entryTime[node] - 1) / 2
    
    return descendants

function eulerTour(node, entryTime, exitTime, time):
    if node == null:
        return
        
    // Record entry time
    time = time + 1
    entryTime[node] = time
    
    // Visit left child
    eulerTour(node.left, entryTime, exitTime, time)
    
    // Visit right child
    eulerTour(node.right, entryTime, exitTime, time)
    
    // Record exit time
    time = time + 1
    exitTime[node] = time

The time complexity is O(n) where n is the number of nodes in the tree.
"""