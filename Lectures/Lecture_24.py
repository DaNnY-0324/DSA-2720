"""
Merge Sort:
Time Complexity: O(n log2 n)

82 12 64 23 91 18 70 20

Divide into 2 equal sub-arrays:
(82 12 64 23) (91 18 70 20)

Divide each sub-array into 2 equal sub-arrays:
(82 12) (64 23) (91 18) (70 20)

Divide each sub-array into 2 equal sub-arrays:
(82) (12) (64) (23) (91) (18) (70) (20)

Merge each pair of sub-arrays:
(12 82) (23 64) (18 91) (20 70)

Merge each pair of sub-arrays:
(12 23 64 82) (18 20 70 91)

Merge each pair of sub-arrays:
(12 18 20 23 64 70 82 91)

Final sorted array:
12 18 20 23 64 70 82 91

"""

"""
Quick Sort:

Hoare [1962]

Avg case Time Complexity: O(n log2 n)
Worst case Time Complexity: O(n^2)

- Selection of Pivot element
    - Always choose the first element form the input array as pivot
    
  0  1  2  3  4  5  6  7  8
(25 12 34 10 30 20 40 18 35)
  ^ pivot

What will be the output after execution of first pass of quick sort? Show All Steps

Idea: "As long as element points by low is <= pivot, low is incremented by 1.
       When you cannot increment low, try incrementing high. As long as element 
       point by high is > pivot, high is decremented by 1.
       When you cannot decrement high then exchange elements pointed by low and high.
       If low <= high repeat step 1 to 4."

* Exchange elements pointed by high and pivot.

  0  1  2  3  4  5  6  7  8
(20 12 18 10 25 30 40 34 35)

(100 210 38 46 200 60 150)

(60 46 38 100 150 200 210)
"""

