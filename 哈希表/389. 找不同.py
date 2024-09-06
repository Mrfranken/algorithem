class Solution(object):
    """
    https://leetcode.cn/problems/find-the-difference/description/
    哈希表
    """
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1

        for item in t:
            if item in d:
                d[item] -= 1
                if d[item] == 0:
                    d.pop(item)
            else:
                return item
        return list(d.keys())[0]
