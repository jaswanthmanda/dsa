# LRU Cache


class DoublyLL(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # initialize empty list
        self.headNode = None
        self.tailNode = None
        self.mpp = {}
        self.cap = capacity

        self.init_empty_list()

    def init_empty_list(self):
        headNode = DoublyLL(-1, -1)
        tailNode = DoublyLL(-1, -1)

        headNode.next = tailNode
        tailNode.prev = headNode

        self.headNode = headNode
        self.tailNode = tailNode

    def insertANode(self, node):
        currNextNode = self.headNode.next
        self.headNode.next = node
        node.prev = self.headNode
        node.next = currNextNode
        currNextNode.prev = node

    def deleteANode(self, node):
        prevNode = node.prev
        nextNode = node.next

        # remove pointers to node
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.mpp:
            return -1

        node = self.mpp[key]  # Get the node
        val = node.val

        # delete the node
        self.deleteANode(node)

        # insert after head
        self.insertANode(node)

        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # check for key
        if key in self.mpp:
            node = self.mpp[key]
            node.val = value

            # delete the node
            self.deleteANode(node)

            self.insertANode(node)

            return

        if len(self.mpp) == self.cap:
            # Get the least recently used node
            node = self.tailNode.prev

            # delete node from map
            del self.mpp[node.key]

            # Delete node from doubly linked list
            self.deleteANode(node)

        newNode = DoublyLL(key, value)

        # insert into map
        self.mpp[key] = newNode

        # insert into dll
        self.insertANode(newNode)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
