from functools import reduce

class Solution(object):
    """
    https://leetcode.cn/problems/single-number/description/
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)