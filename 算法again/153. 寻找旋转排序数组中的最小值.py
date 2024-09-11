class Solution(object):
    """
    跟右值进行比较，不断搜索右边界
    如果中值 < 右值，则最小值右半边，收缩右边界到mid位置
    如果中值 > 右值，中值在左半边，最小值在右半边，收缩左边界
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        return nums[left]


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(Solution().findMin(nums))
