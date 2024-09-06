class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[len(cost)]


if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    # print(s.minCostClimbingStairs([10, 15, 20]))
