class Solution(object):
    def stockManagement(self, stock):
        """
        :type stock: List[int]
        :rtype: int
        https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solutions/624665/jian-zhi-offer-11-xuan-zhuan-shu-zu-de-z-rur2/
        https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solutions/341051/labuladong-er-fen-fa-mo-ban-shi-xiao-liao-ma-by-41/
        二分查找
        """
        left = 0
        right = len(stock) - 1
        while left < right:
            mid = left + (right - left) // 2
            if stock[mid] > stock[right]:
                left = mid + 1
            else:
                right = mid
        return stock[left]

        left = 0
        right = len(stock) - 1
        while left <= right:
            mid = (left + right) // 2
            if stock[mid] > stock[right]:
                left = mid + 1
            elif stock[mid] < stock[right]:
                right = mid
            else:
                right -= 1
        return stock[left]


if __name__ == '__main__':
    s = Solution()
    stock = [4, 5, 6, 7, 0, 1, 2]
    # stock = [4, 5, 8, 3, 4]
    # stock = [5, 7, 9, 1, 2]
    # stock = list(range(10))
    stock = [3, 1, 1]
    print(s.stockManagement(stock))
