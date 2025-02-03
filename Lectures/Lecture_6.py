# Expression    Notations
# a + b      => infix notation - operand is in between 2 operators
# -a         => prefix (or polish) notation - operand is before operator
# ab +       => postfix (or reversal polish) notation - operand is after operator

# Operators
# 1. Unary Operators - uses 1 operand
# 2. Binary Operators - uses 2 operands
# 3. Ternary Operators - uses 3 operands

x = 5
print(-x)

# Convert the given infix notation to postfix notation

# Infix: 
# a + b * c
# a * b + c
# a + b * c + d
# a * b - c * d
# a * b + c / (d - e) * f
# (A + B) * C - D
# A + B * (C + D) / F + D * E
# (a + b) * (c + d)
# 10 5 + 60 6 / * 8 -

# Postfix: 
# abc*+
# ab*c+
# abc*+d+
# ab*cd*-
# ab*cde-/f*+
# AB+C*D-
# ABCD+*F/DE*+
# ab+cd+*
# 142
