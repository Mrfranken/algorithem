class MyHashSet(object):

    def __init__(self):
        self.buckets = [[0] * 10 for _ in range(10)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        row = key // 1000
        col = key % 1000
        self.buckets[row][col] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        row = key // 1000
        col = key % 1000
        self.buckets[row][col] = 0

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        row = key // 1000
        col = key % 1000
        return self.buckets[row][col] == 1


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.add(2)
obj.remove(2)
param_3 = obj.contains(2)
