class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        https://leetcode.cn/problems/valid-anagram/description/
        哈希表
        """
        d = {}
        c = {}
        for item in s:
            d[item] = d.get(item, 0) + 1
        for item in t:
            c[item] = c.get(item, 0) + 1
        return d == c

