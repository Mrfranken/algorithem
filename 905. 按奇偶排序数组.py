class Solution(object):
    """
    https://leetcode.cn/problems/sort-array-by-parity/description/
    双指针
    """
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        tmp_left = None
        tmp_right = None
        while left < right:
            if nums[left] % 2 == 0:
                # even
                left += 1
            else:
                # odd
                tmp_left = left

            if nums[right] % 2 != 0:
                # even
                right -= 1
            else:
                # odd
                tmp_right = right

            if tmp_left is not None and tmp_right is not None:
                nums[tmp_left], nums[tmp_right] = nums[tmp_right], nums[tmp_left]
                tmp_left = None
                tmp_right = None
                left += 1
                right -= 1
        return nums


if __name__ == '__main__':
    nums = [3, 1, 2, 4]
    s = Solution()
    print(s.sortArrayByParity(nums))
