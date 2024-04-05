
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
