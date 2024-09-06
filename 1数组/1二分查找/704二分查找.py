class Solution(object):
    """
    https://leetcode.cn/problems/binary-search/description/
    """

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    # nums = [5]
    # target = 5
    v = s.search(nums, target)
    print(v)
