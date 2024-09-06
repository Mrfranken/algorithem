class NumArray(object):
    """
    https://leetcode.cn/problems/range-sum-query-immutable/solutions/2693498/qian-zhui-he-ji-qi-kuo-zhan-fu-ti-dan-py-vaar/
    https://leetcode.cn/problems/range-sum-query-immutable/description/
    前缀和
    动态规划
    """

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.s = [0] * (len(nums) + 1)
        for index, num in enumerate(nums):
            self.s[index + 1] = self.s[index] + num

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.s[right + 1] - self.s[left]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(2, 5)
print(param_1)
