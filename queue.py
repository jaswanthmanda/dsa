class Node:
    def __init__(self, val):
        """Constructor"""
        self.val = val
        self.next = None

class MyQueueSupporter:
    def __init__(self, val):
        """Constructor"""

class MyQueue:
    """Linked List implementation of Queue"""

    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0

    def size(self):
        return self.sz

    def isEmpty(self):
        return (self.sz == 0)

    def getFront(self):
        return self.front.val

    def getRear(self):
        return self.rear.val

    def enqueue(self, x):
        temp = Node(x)
        if self.rear == None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.sz += 1

    def deque(self):
        if self.front == None:
            return None
        else:
            res = self.front.val
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self.sz -= 1
            return res

q = MyQueue()

q.enqueue(10)

q.enqueue(20)

q.enqueue(30)

print(q.deque())

print(q.size())