class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            dp[i] = dp[i - 1] + nums[i - 1]
        return dp[1:]


if __name__ == '__main__':
    s = Solution()
    print(s.runningSum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
