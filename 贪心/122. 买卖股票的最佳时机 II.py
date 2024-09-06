class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/
        8.13 贪心
        """
        a = 0
        for index, num in enumerate(prices[:-1]):
            profit = prices[index + 1] - num
            if profit > 0:
                a += profit

        return a


if __name__ == '__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(prices))
