class Solution(object):
    """
    动态规划

    设定dp[i]当偷到第i个房子的时候的总金额

    那到底要不要偷第i个方式呢：有两种不同的偷法
    1. 偷i - 2个房子，然后再偷第i个方式
    2. 偷i - 1个房子，然后第i个方式不偷
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))
