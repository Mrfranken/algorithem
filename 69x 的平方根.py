# class Solution(object):
#     def mySqrt(self, x):
#         """
#         给你一个非负整数 x ，计算并返回 x 的算术平方根 。
#
#         由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
#         注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
#         """
#         left, right = 0, x // 2
#         while left <= right:
#             middle = (right + left) // 2  # 注意这里，虽然是用二分查找法，但因为寻找的就是数字本身，而不是下标，所以要用加号
#             num = middle * middle
#             if num > x:
#                 right = middle - 1
#                 continue
#             if num < x:
#                 left = middle + 1
#                 continue
#             if num == x:
#                 return middle
#         return left
#
#
# if __name__ == '__main__':
#     s = Solution()
#     v = s.mySqrt(9000000000)
#     print(v)
