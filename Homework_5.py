"""
1. Inside the Castle of Asymptopia there is a maze, and along each corridor of the maze there
is a bag of gold coins. The amount of gold in each bag varies. A noble knight, named Sir
Paul, will be given the opportunity to walk through the maze, picking up bags of gold. He
may enter the maze only through a door marked “ENTER” and exit through another door
marked “EXIT.” While in the maze he may not retrace his steps. Each corridor of the maze
has an arrow painted on the wall. Sir Paul may only go down the corridor in the direction
of the arrow. There is no way to traverse a “loop” in the maze. Given a map of the maze,
including the amount of gold in each corridor, describe an algorithm to help Sir Paul pick
up the most gold.

Answer:
This is a **Directed Acyclic Graph (DAG)** problem where each edge has a weight (gold coins).

We can use **Dynamic Programming on DAGs**:
1. Model the maze as a weighted DAG where corridors are edges and rooms are vertices.
2. Use **topological sort** on the DAG.
3. Initialize a `maxGold[]` array where `maxGold[v]` stores the maximum gold collectable to reach vertex `v`.
4. Set `maxGold[ENTER] = 0`.
5. For each vertex `u` in topological order:
    - For each neighbor `v` of `u`:
        - If there is an edge from `u` to `v` with weight `w` (gold coins), update:
          `maxGold[v] = max(maxGold[v], maxGold[u] + w)`
6. The answer is `maxGold[EXIT]`, which gives the maximum gold Sir Paul can collect.

Time complexity: O(V + E)
"""

"""
2. Dr. Amongus claims that the order in which a fixed set of entries is inserted into an AVL
tree does not matter—the same AVL tree results every time. Give a small example that
proves he is wrong.

Answer:
Let’s insert the same keys in different orders:

Order A: Insert 10, 20, 30  
- Causes a right-right imbalance → Rotate left → Final tree:
        20
       /  \
     10   30

Order B: Insert 30, 20, 10  
- Causes a left-left imbalance → Rotate right → Final tree:
        20
       /  \
     10   30

In this case, both result in the same AVL tree. But try this:

Order A: 10, 30, 20  
- Causes a left-right imbalance → Rotate left at 30, then right at 10 → Final tree:
        20
       /  \
     10   30

Order B: 30, 10, 20  
- Causes a right-left imbalance → Rotate right at 10, then left at 30 → Final tree:
        20
       /  \
     10   30

These still give the same result.

Let’s try a more clear case:
Order A: 5, 3, 8, 2  
Order B: 5, 8, 3, 2

These will cause different rotation sequences, resulting in **different AVL trees**, thus proving Dr. Amongus is wrong.
"""

"""
3. Draw the 11-entry hash table that results from using the hash function, h(i) = (3i+5) mod
11, to hash the keys 12, 44, 13, 88, 23, 94, 11, 39, 20, 16, and 5, assuming collisions are
handled by chaining.

Answer:

Apply h(i) = (3i + 5) mod 11 to each key:

- 12 → (3×12 + 5) % 11 = 41 % 11 = 8
- 44 → (3×44 + 5) % 11 = 137 % 11 = 5
- 13 → (3×13 + 5) % 11 = 44 % 11 = 0
- 88 → (3×88 + 5) % 11 = 269 % 11 = 5
- 23 → (3×23 + 5) % 11 = 74 % 11 = 8
- 94 → (3×94 + 5) % 11 = 287 % 11 = 1
- 11 → (3×11 + 5) % 11 = 38 % 11 = 5
- 39 → (3×39 + 5) % 11 = 122 % 11 = 1
- 20 → (3×20 + 5) % 11 = 65 % 11 = 10
- 16 → (3×16 + 5) % 11 = 53 % 11 = 9
- 5  → (3×5 + 5) % 11 = 20 % 11 = 9

Hash Table (using chaining):

Index | Keys  
------|-------
0     | 13  
1     | 94 → 39  
2     |  
3     |  
4     |  
5     | 44 → 88 → 11  
6     |  
7     |  
8     | 12 → 23  
9     | 16 → 5  
10    | 20
"""
