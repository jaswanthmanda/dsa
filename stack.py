
# stack with linkedlist
class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class StackwithLL:

    def __init__(self) -> None:
        self.head = None
        self.stack_size = 0

    def push(self, val):
        temp_node = Node(val)
        temp_node.next = self.head
        self.head = temp_node
        self.stack_size += 1

    def size(self):
        return self.stack_size

    def peek(self):
        if self.head == None:
            print("Stack is empty")

        return self.head.val

    def pop(self):
        if self.head == None:
            print("Stack is empty")

        res = self.head.val
        self.head = self.head.next
        self.stack_size -= 1
        return res

s = StackwithLL()

s.push(10)

s.push(20)

s.push(30)

print(s.pop())

print(s.peek())

print(s.size())

# <-- -->

# infix to postfix
"""
1) symbol priority
    - ^ - priority 1
    -  * / - priority 2
    - + - - priority 3
2) no two operators of same priority can stay together in stack
    - if '/' is the top of the stack and '*' to be inserted then we have to pop '/' and insert '*'
3) when high priority is on top of stack pop that element and insert low priority into the stack
    - '*' is the top of stack and the element to be inserted is '-'
      then we have to pop the '*' and insert '-'
4) If any element like '(+)' should not be present in stack
    - if the stack contains
        - +
        - (
      and item to be inserted is ')' the final combination is '+' in closed bracket.
      So the parameters inside stack upto '(' should have to be popped.
"""

def infix_to_prefix(inf_exp: str) -> str:
    """Converts infix expression to postfix expression"""
    stack = []
    res = ""
    priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    for char in inf_exp:
        if char == "(":
            stack.append(char)
        elif char == ")":
            while (
                len(stack) > 0 and
                stack[-1] != "("
            ):
                ele = stack.pop()
                res += ele
            stack.pop()
        elif (
            char == "+" or
            char == "-" or
            char == "*" or
            char == "/" or
            char == "^"
        ):
            while (
                len(stack) > 0
                and stack[-1] not in ["(", ")"]
                and priority[stack[-1]] >= priority[char]
            ):
                ele = stack.pop()
                res += ele
            stack.append(char)
        else:
            res += char

    while (
        len(stack) > 0
    ):
        ele = stack.pop()
        res += ele

    return res

# call the function
print(infix_to_prefix("a+b*(c^d-e)^(f+g*h)-i"))

def prefix_to_infix(inf_exp: str) -> str:
    """Converts prefix expression to infix expression"""
    """
    Rules:
        - Reverse the prefix expression
        - if any operator arrived , pop two operands from stack and make a
          operation node with that operand and push it post adding parathesis.
          Ex: [c, d] in stack, char - '/' -> ['(c/d)'] in stack
    """

    stack = []
    inf_exp = inf_exp[::-1]
    for char in inf_exp:
        if char in ["+", "-", "*", "/", "^"]:
            ele1 = stack.pop()
            ele2 = stack.pop()
            final_str = f"({ele1}{char}{ele2})"
            stack.append(final_str)
        else:
            stack.append(char)

    res = stack.pop()

    return res

# call func
"""
*-A/BC-/AKL
LKA/-CB/A-*
[A, K, L]
[(A/K), L]
"""
print(prefix_to_infix("*-A/BC-/AKL"))

def postfix_to_infix(postfix):
    """
    Converts postfix expression to infix
    """
    """
    Rules to convert:
        - reverse is not required
        - if any operator arrived , pop two operands from stack and make a
          operation node with that operand (where second operand of the stack comes first)
          and push it post adding parathesis.
          Ex: [c, d] in stack, char - '/' -> ['(d/c)'] in stack
    """
    stack = []
    for char in postfix:
        if char in ["+", "-", "*", "/", "^"]:
            ele2 = stack.pop()
            ele1 = stack.pop()
            stack.append("("+ele1+char+ele2+")")
        else:
            stack.append(char)

    res = stack.pop()
    return res

# call the func
print(postfix_to_infix("ab*c+"))