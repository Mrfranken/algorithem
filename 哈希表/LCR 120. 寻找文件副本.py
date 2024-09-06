class Solution(object):
    def findRepeatDocument(self, documents):
        """
        :type documents: List[int]
        :rtype: int
        https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
        哈希表
        """
        d = {}
        for item in documents:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1

        for k, v in d.items():
            if v >= 2:
                return k