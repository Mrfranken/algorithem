class Solution(object):
    """
    https://leetcode.cn/problems/search-insert-position/description/
    """

    def searchInsert(self, nums, target):
        #     """
        #     :type nums: List[int]
        #     :type target: int
        #     :rtype: int
        #     """
        #     left, right = 0, len(nums) - 1
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if nums[mid] > target:
        #             right = mid - 1
        #         elif nums[mid] < target:
        #             left = mid + 1
        #         else:
        #             return mid
        #     return right + 1

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
        return start


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 5, 6]
    # target = 9
    target = 2
    v = s.searchInsert(nums, target)
    print(v)
