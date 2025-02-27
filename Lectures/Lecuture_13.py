# Create a Binary Search Tree for keys 45, 39, 56, 12, 34, 78, 32, 10, 89, 54, 67, 81

#         45
#      39     56
#   12  34  54  78
# 10 32       67  89
#          81

# Given a preorder 40, 30, 32, 35, 80, 90, 100, 120 of some BST, find its postorder traversal.

#         40
#      30    80
#         32    90
#           35     100
#                     120

# Preorder: 40, 30, 32, 35, 80, 90, 100, 120
# Inorder: 30, 32, 35, 40, 80, 90, 100, 120
# Postorder: 35, 32, 30, 120, 100, 90, 80, 40

# Deletion of node x
# Case 1: x is a leaf node
# Case 2: x has one child
# Case 3: x has two children