from typing import List

class Solution:
    """
    https://leetcode.cn/problems/squares-of-a-sorted-array/description/
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1
        res = [None] * len(nums)

        while left <= right:
            left_value = nums[left]
            right_value = nums[right]
            if left_value ** 2 < right_value ** 2:
                res[index] = right_value ** 2
                right -= 1
            elif left_value ** 2 >= right_value ** 2:
                res[index] = left_value ** 2
                left += 1
            index -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-4, -1, 0, 3, 10]
    s.sortedSquares(nums)
