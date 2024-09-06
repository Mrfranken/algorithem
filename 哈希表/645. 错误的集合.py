class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for k, v in d.items():
            if v > 1:
                return [k, k + 1]
