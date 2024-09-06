class Solution(object):
    """
    https://leetcode.cn/problems/majority-element/description/
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        limit = (len(nums)+1)//2
        d = {}
        for num in nums:
            count = d.get(num, 0) + 1
            d[num] = count
            if count > limit:
                return num


