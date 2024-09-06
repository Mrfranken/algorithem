class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solutions/1692872/by-jyd-cu90/
        贪心
        """
        cost = float('+inf')
        profit = 0
        for price in prices:
            if price < cost:
                cost = price
            tmp = price - cost
            if tmp > profit:
                profit = tmp
        return profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
