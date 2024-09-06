class Solution(object):
    """
    当nums长度为3：  a = b
    当nums长度大于3：
        if 正数长度小于3个，那最大的应该是两个最小的负数 和 最大的正数的乘积
        if 负数长度小于3个，那最大的应该是最大的3个正数的乘积
    """
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]
        return max(a, b)
