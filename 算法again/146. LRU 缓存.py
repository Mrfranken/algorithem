class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def delete(self, node):
        """
        删除时prev需要连接next
        同时next也需要连接prev
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        tmp = self.head.next
        self.head.next = node
        tmp.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1

        node = self.d[key]
        self.delete(node)
        self.insert(node)
        return node.val

    def put(self, key, value):
        """
        如果key在d中:更新（删除node 插入node）
        如果key不在d中：
        检查空间是否full：
        1. full,    删掉tailnode然后insert
        2. not full,直接insert

        """
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.delete(node)
            self.insert(node)
            return

        if len(self.d) == self.capacity:
            node = self.tail.prev
            self.delete(node)
            del self.d[node.key]

        node = Node(key, value)
        self.d[key] = node
        self.insert(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
