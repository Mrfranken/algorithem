class MyHashMap(object):
    """
    https://www.hello-algo.com/chapter_hashing/hash_map/
    哈希表 拉链法
    https://leetcode.cn/problems/design-hashmap/description/
    """

    def __init__(self):
        self.buckets = [[-1] * 1000 for _ in range(10001)]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        row = key // 1000
        col = key % 1000
        self.buckets[row][col] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        row = key // 1000
        col = key % 1000
        return self.buckets[row][col]

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        row = key // 1000
        col = key % 1000
        self.buckets[row][col] = -1