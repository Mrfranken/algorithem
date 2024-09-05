from typing import List


class Solution:
    """
    https://leetcode.cn/problems/squares-of-a-sorted-array/description/
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                res.insert(0, nums[right] ** 2)
                right -= 1
            else:
                res.insert(0, nums[left] ** 2)
                left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-4, -1, 0, 3, 10]
    nums = [-7, -3, 2, 3, 11]
    s.sortedSquares(nums)
