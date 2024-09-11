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
            left = 0
            right = len(nums) - 1

            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    return middle
            return -1

        start = search_target(nums, target)
        if start == -1:
            return [-1, -1]

        left, right = start, start
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1

        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1

        return [left, right]


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2]
    nums = [5, 7, 7, 8, 8, 10]
    # target = 9
    target = 8
    v = s.searchRange(nums, target)
    print(v)
