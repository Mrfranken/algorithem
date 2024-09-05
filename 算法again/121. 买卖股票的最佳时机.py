class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solutions/1692872/by-jyd-cu90/
        贪心
        """
        cost = float('inf')
        profit = 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit

