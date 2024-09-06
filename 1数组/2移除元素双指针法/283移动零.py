class Solution(object):
    """
    https://leetcode.cn/problems/move-zeroes/description/
    """

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a, b = 0, 0
        while a < len(nums):
            if nums[a] != 0:
                nums[b], nums[a] = nums[a], nums[b]
                b += 1
            a += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    n = [0, 1, 0, 3, 12]
    print(s.moveZeroes(n))
