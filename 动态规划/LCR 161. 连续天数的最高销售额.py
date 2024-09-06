class Solution(object):
    def maxSales(self, sales):
        """
        :type sales: List[int]
        :rtype: int
        """
        dp = [None] * len(sales)
        dp[0] = sales[0]
        for i in range(1, len(sales)):
            dp[i] = max(dp[i - 1] + sales[i], sales[i])
        return max(dp)

if __name__ == '__main__':
    s = Solution()
    print(s.maxSales(sales=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
