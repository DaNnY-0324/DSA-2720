# TreeNode class
class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

# BinarySearchTree class
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    # Insert method
    def insert(self, val: int) -> None:
        self.root = self._insert_recursive(self.root, val)

    def _insert_recursive(self, node: TreeNode, val: int) -> TreeNode:
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        return node

    # Search method
    def search(self, val: int) -> bool:
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node: TreeNode, val: int) -> bool:
        if node is None:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)

    # Delete method
    def delete(self, val: int) -> None:
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, node: TreeNode, val: int) -> TreeNode:
        if node is None:
            return None

        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children:
            # Get the inorder successor (smallest in the right subtree)
            min_larger_node = self._find_min(node.right)
            node.val = min_larger_node.val
            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, min_larger_node.val)

        return node

    def _find_min(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Inorder traversal
    def inorder_traversal(self) -> list[int]:
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: TreeNode, result: list[int]) -> None:
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)

    # Preorder traversal
    def preorder_traversal(self) -> list[int]:
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: TreeNode, result: list[int]) -> None:
        if node is not None:
            result.append(node.val)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    # Postorder traversal
    def postorder_traversal(self) -> list[int]:
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: TreeNode, result: list[int]) -> None:
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.val)

# Usage example
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(15)
    bst.insert(17)
    bst.insert(10)
    bst.insert(11)
    bst.insert(13)
    bst.insert(12)

    print("Preorder Traversal:", bst.preorder_traversal())
    print("Inorder Traversal:", bst.inorder_traversal())
    print("Postorder Traversal:", bst.postorder_traversal())

    print("Search 13:", bst.search(13))
    print("Search 100:", bst.search(100))

    print("Deleting 15")
    bst.delete(15)
    print("Inorder Traversal after deletion:", bst.inorder_traversal())
