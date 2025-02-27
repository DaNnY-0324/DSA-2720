def checkBalancedParenthesis(s):
    if not s:
        raise TypeError
    
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != matching_bracket[char]:
                return "Unbalanced"
            stack.pop()
    
    return "Balanced" if not stack else "Unbalanced"

def getUnbalancedPositions(s):
    if not s:
        raise TypeError
    
    stack = []  # Stores (index, character)
    unbalanced_indices = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for i, char in enumerate(s):
        if char in "({[":
            stack.append((i, char))
        elif char in ")}]":
            if not stack or stack[-1][1] != matching_bracket[char]:
                unbalanced_indices.append(i)  # Unmatched closing bracket
            else:
                stack.pop()
    
    # Any remaining items in stack are unmatched opening brackets
    unbalanced_indices.extend([index for index, _ in stack])
    
    return sorted(unbalanced_indices)

# Sample Test Cases
print(checkBalancedParenthesis("()"))  # Balanced
print(checkBalancedParenthesis("(]"))  # Unbalanced
print(getUnbalancedPositions("()"))  # []
print(getUnbalancedPositions("(]"))  # [0, 1]
print(getUnbalancedPositions("(a+b"))  # [0]
print(getUnbalancedPositions("a + (b * c] - {d / e)"))  # [4, 10, 14, 20]
