class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/description/
        """

        def search_target(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        start = search_target(nums, 0)
        end = search_target(nums, 1)
        return max(start, len(nums[end:]))


if __name__ == '__main__':
    s = Solution()
    nums = [-2, -1, -1, 1, 2, 3]
    nums = [-3, -2, -1, 0, 0, 1, 2]
    nums = [5, 20, 66, 1314]
    print(s.maximumCount(nums))
