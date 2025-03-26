class TreeNode:
    """
    Represents a node in the expression tree.

    Attributes:
        value (int | str): Stores either an operand (integer) or an operator (+, -, *, /).
        left (TreeNode | None): Left child node.
        right (TreeNode | None): Right child node.
    """
    def __init__(self, value):
        """
        Initializes a TreeNode with a given value.

        Args:
            value (int | str): The value to store in the node.
        """
        self.value = value
        self.left = None
        self.right = None


class ExpressionTree:
    """
    Builds and evaluates an expression tree from a postfix expression.

    Attributes:
        root (TreeNode | None): The root node of the constructed expression tree.
    """
    def __init__(self, postfix_expr: str) -> None:
        """
        Initializes the expression tree by constructing it from the given postfix expression.

        Args:
            postfix_expr (str): A space-separated string of operands and operators in postfix notation.
        """
        self.root = self.construct_expression_tree(postfix_expr)

    def construct_expression_tree(self, postfix: str) -> TreeNode:
        """
        Constructs an expression tree from a postfix expression.

        Args:
            postfix (str): A space-separated string of operands and operators in postfix notation.

        Returns:
            TreeNode | None: The root of the constructed tree.
        """
        if not postfix:
            return None

        stack = []
        tokens = postfix.split()

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                # Operator: Pop two operands from stack
                if len(stack) < 2:
                    raise ValueError("Invalid postfix expression")

                # Create a new node with the operator
                node = TreeNode(token)

                # The right operand is popped first (stack is LIFO)
                node.right = stack.pop()
                node.left = stack.pop()

                # Push the new subtree onto the stack
                stack.append(node)
            else:
                # Operand: Create a new node and push onto stack
                try:
                    value = int(token)
                except ValueError:
                    try:
                        value = float(token)
                    except ValueError:
                        raise ValueError(f"Invalid token: {token}")

                stack.append(TreeNode(value))

        # The stack should now contain only the root node
        if len(stack) != 1:
            raise ValueError("Invalid postfix expression")

        return stack[0]

    def evaluate_expression(self) -> int | float:
        """
        Returns the evaluated result of the expression tree.

        Returns:
            int | float: The evaluated result of the expression.
            Returns float('inf') for division by zero.
        """
        return self._evaluate(self.root)

    def _evaluate(self, node: TreeNode) -> int | float:
        """
        Recursively evaluates the expression tree.

        Args:
            node (TreeNode): The current node to evaluate.

        Returns:
            int | float: The evaluated result of the subtree.
        """
        if node is None:
            return 0

        # Leaf node (operand)
        if node.left is None and node.right is None:
            return node.value

        # Evaluate the left and right subtrees
        left_val = self._evaluate(node.left)
        right_val = self._evaluate(node.right)

        # Apply the operator
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            # Handle division by zero
            if right_val == 0:
                return float('inf')
            return left_val / right_val

        # Should not reach here if the expression is valid
        raise ValueError(f"Invalid operator: {node.value}")

    def get_inorder_expression(self) -> str:
        """
        Returns the infix expression with proper parentheses.

        Returns:
            str: The infix expression with proper parentheses.
        """
        return self._get_inorder(self.root)

    def _get_inorder(self, node: TreeNode) -> str:
        """
        Recursively builds the infix expression.

        Args:
            node (TreeNode): The current node to process.

        Returns:
            str: The infix expression of the subtree.
        """
        if node is None:
            return ""

        # Leaf node (operand)
        if node.left is None and node.right is None:
            return str(node.value)

        # Get expressions for left and right subtrees
        left_expr = self._get_inorder(node.left)
        right_expr = self._get_inorder(node.right)

        # Add parentheses around the expression
        return f"({left_expr}{node.value}{right_expr})"