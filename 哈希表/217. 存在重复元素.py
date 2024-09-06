class Solution(object):
    """
    https://leetcode.cn/problems/contains-duplicate/description/
    哈希表
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for num in nums:
            if d.get(num, 0) >= 2:
                return True
            d[num] = d.get(num, 0) + 1

        for k, v in d.items():
            if v >= 2:
                return True
        return False
