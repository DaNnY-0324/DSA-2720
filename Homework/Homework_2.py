"""
Instructions: Please complete the following questions on a separate sheet of paper. After you have
finished, scan your work and upload it to Homework Assignment 2 in our Gradescope for the CSC 2720
DATA STRUCTURES XLS Group ACS11 Spring Semester 2025 course.
"""

"""
1. Describe a method for performing a card shuffle of a list of 2n elements, by converting it into two
lists. A card shuffle is a permutation where a list L is cut into two lists, L1 and L2, where L1 is the
first half of L and L2 is the second half of L, and then these two lists are merged into one by taking
the first element in L1, then the first element in L2, followed by the second element in L1, the
second element in L2, and so on.

To perform a card shuffle of a list L containing 2n elements by converting it into two lists:

Split the original list into two halves:

L1 contains elements at positions 0 to n - 1 (first half of L).
L2 contains elements at positions n to 2n - 1 (second half of L).
Create a new empty result list, named shuffled.

Interleave the elements from L1 and L2 by alternating:

Take the first element from L1, then the first from L2.
Take the second element from L1, then the second from L2.
Continue this pattern until all elements are merged.
Return the shuffled list, which now contains all elements in their shuffled order.

Complexity:
Time Complexity: O(n)
Space Complexity: O(n)

"""

"""
2. Suppose you have a stack S containing n elements and a queue Q that is initially empty. Describe
how you can use Q to scan S to see if it contains a certain element x, with the additional constraint
that your algorithm must return the elements back to S in their original order. You may only use
S, Q, and a constant number of other variables.

You have a stack S containing n elements and an empty queue Q. You need to scan S to check if it contains a certain element x, while ensuring that S is returned to its original order.

Algorithm:
Initialize:

An empty queue Q.
A boolean variable found = false.
Scan stack S:

While S is not empty:
Pop the top element from S.
If the element equals x, set found = true.
Enqueue the element into Q.
Restore stack S:

While Q is not empty:
Dequeue an element from Q.
Push the element back onto S.
At this point, S is reversed from its original order.
Reverse S back to original order:

Repeat steps 2 and 3 one more time.
This puts S back in its original order.
Return the boolean value found.

Complexity:
Time Complexity: O(n)
Space Complexity: O(1) extra space (excluding S and Q), with only a constant number of variables used.

"""

"""
3. Suppose Bob has four cows that he wants to take across a bridge, but only one yoke, which can
hold up to two cows, side by side, tied to the yoke. The yoke is too heavy for him to carry across
the bridge, but he can tie (and untie) cows to it in no time at all. Of his four cows, Mazie can cross
the bridge in 2 minutes, Daisy can cross it in 4 minutes, Crazy can cross it in 10 minutes, and Lazy
can cross it in 20 minutes. Of course, when two cows are tied to the yoke, they must go at the
speed of the slower cow. Describe how Bob can get all his cows across the bridge in 34 minutes.
Hint: Use either stack or queue to solve the problem.

Problem Recap:
Bob has four cows with the following crossing times:

Mazie: 2 minutes
Daisy: 4 minutes
Crazy: 10 minutes
Lazy: 20 minutes
Only two cows can cross at a time with a single yoke. When two cows cross together, they must go at the pace of the slower cow. Bob needs to get all cows across the bridge in 34 minutes.

Optimal Strategy:
Mazie and Daisy cross first ➔ 4 minutes (Mazie and Daisy are on the other side).
Mazie returns ➔ 2 minutes (Mazie is back on the starting side).
Crazy and Lazy cross together ➔ 20 minutes (Crazy and Lazy are now across).
Daisy returns ➔ 4 minutes (Daisy comes back to starting side).
Mazie and Daisy cross again ➔ 4 minutes (Mazie and Daisy cross the bridge again).
Total Time Calculation:
4 + 2 + 20 + 4 + 4 = 34 minutes


"""