# Tree
# nonlinear data structure
# Hierachical data structure
# Contains zero or more nodes

#Ex. Tree
#    A
#  B   C
# D E   G 
#  F     H

# Binary Tree (BT)
# * Also known as Proper / Full BT
# Each node has at most 2 children
# Every child is either left or right child

# Internal Node (Non-leaf Node)
# Node with at least one child

# External Node (Leaf Node)
# Node with no children

# Sibling Node
# Nodes with the same parent

# Ancestor Node:
# A node is an ancestor of itself and all its descendants
# Ex. Ancestor of H: G,C,A 

# Descendant Node:
# A node is a descendant of itself and all its ancestors
# Ex. Descendant of B: D,E,F 

# Types of BT
# 1) Strictly BT:
#    Each internal node has exactly 2 children

# Level of a Node:
# Root node is at level 0
# Level of a node = length of the path from root to that node
# Ex. Level of A: 0, Level of B: 1, Level of D: 2

# Height of a Node:
# Maximum level of any leaf

# In general, level d will have at most 2^d nodes

# 2) Complete BT:
#   All levels are completely filled except possibly the last level

# i) Strictly BT
# ii) All leaf nodes are at level 'd'

# Tree Traversal:
# "Visiting all nodes of a tree"

# Tree Traversal Methods:
# 1) Preorder (or depth-first): Data->Left->Right
# 2) Inorder (or systematic): Left->Data->Right
# 3) Postorder (or depth-last): Left->Right->Data
# 4) Reverse Postorder : Right->Left->Data

#   A
# B   C

# Preorder: A, B, C
# i) Visit Node
# ii) Traverse Left Subtree in Preorder 
# iii) Traverse Right Subtree in Preorder

#         A
#     B       C
#   E   F   D   
#     G  H   I

# Preorder: A, B, E, G, F, H, C, D, I

# Inorder: B, A, C
# i) Traverse Left Subtree in Inorder
# ii) Visit Node
# iii) Traverse Right Subtree in Inorder

#         A
#     B       C
#   E   F   D   
#     G  H   I

# Inorder: E, B, F, G, H, A, C, D, I

# Postorder: B, C, A
# i) 
# ii) 
# iii) 

#         A
#     B       C
#   E   F   D   
#     G  H   I

# Postorder: 




