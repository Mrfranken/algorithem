class Solution(object):
    """
    https://leetcode.cn/problems/sqrtx/description/
    """
    def mySqrt(self, x):
        left, right = 0, x
        target = None

        while left <= right:
            mid = (left + right) // 2
            temp = mid ** 2
            if temp > x:
                right = mid - 1
            else:
                # target = mid
                left = mid + 1

        if left ** 2 > x:
            return left - 1

        return left


if __name__ == '__main__':
    s = Solution()
    a = s.mySqrt(39)
    print(a)



# class Solution(object):
#     """
#     367
#     """
#     def isPerfectSquare(self, x):
#         left, right = 0, x
#         target = None
#
#         while left <= right:
#             mid = (left + right) // 2
#             temp = mid ** 2
#             if temp > x:
#                 right = mid - 1
#             elif temp < x:
#                 left = mid + 1
#             else:
#                 return True
#
#         return False
#
#
# if __name__ == '__main__':
#     s = Solution()
#     print(s.isPerfectSquare(2))
