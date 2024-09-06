class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        https://leetcode.cn/problems/arranging-coins/description/
        二分法 相当于求最大正整数
        """
        left, right = 1, n

        def cal(mid):
            return (1 + mid) * mid // 2

        while left <= right:
            # mid = (left + right) // 2
            mid = left + (right - left) // 2
            value = cal(mid)
            if value == n:
                return mid
            elif value > n:
                right = mid - 1
            else:
                left = mid + 1

        # if cal(left) > n:
        #     return left - 1
        return left - 1


if __name__ == '__main__':
    s = Solution()
    print(s.arrangeCoins(1))
    print(s.arrangeCoins(2))
    print(s.arrangeCoins(3))
    print(s.arrangeCoins(6))
    print(s.arrangeCoins(7))
