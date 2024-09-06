"""

"""


class Solution(object):
    """
    https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
    """

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def search_target(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                # if nums[mid] > target:
                #     right = mid - 1
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        start = search_target(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = search_target(nums, target + 1) - 1
        return [start, end]

        # index1 = search_target(nums, target)
        # if index1 == -1:
        #     return [-1, -1]
        #
        # left, right = index1, index1
        # while left - 1 >= 0 and nums[left - 1] == target:
        #     left -= 1
        #
        # while right + 1 <= len(nums) - 1 and nums[right + 1] == target:
        #     right += 1
        #
        # return [left, right]


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2]
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    # target = 1
    v = s.searchRange(nums, target)
    print(v)
