class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        res = prices
        for index, price in enumerate(prices):
            while stack and price <= prices[stack[-1]]:
                price_index = stack.pop()
                res[price_index] = prices[price_index] - price
            stack.append(index)
        return res


if __name__ == '__main__':
    s = Solution()
    prices = [8, 4, 6, 2, 3]
    print(s.finalPrices(prices))
