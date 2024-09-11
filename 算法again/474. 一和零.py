from collections import Counter

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (cap + 1) for _ in range(len(strs) + 1)]
        for s in strs:

    def counter(self, s):
        counter = Counter(s)
        return (counter[0], counter[1])