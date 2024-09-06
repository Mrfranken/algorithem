from collections import OrderedDict

class Solution(object):
    def dismantlingAction(self, arr):
        """
        :type arr: str
        :rtype: str
        https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
        哈希表
        """
        d = OrderedDict()
        for item in arr:
            d[item] = d.get(item, 0) + 1


        outcome = list(filter(lambda x: x[-1] == 1, d.items()))
        if not outcome:
            return ' '
        return outcome[0][0]
