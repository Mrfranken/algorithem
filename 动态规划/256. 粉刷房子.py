class Solution:
    def minCost(self, costs):
        dp = [[None for _ in range(3)] for _ in range(len(costs))]

        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for i in range(1, len(costs)):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

        return min(dp[-1])


if __name__ == '__main__':
    s = Solution()
    s.minCost([[14, 2, 11], [11, 14, 5], [14, 3, 10]])
