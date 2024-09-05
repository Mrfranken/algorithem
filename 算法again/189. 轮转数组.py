class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    # nums = [-1, -100, 3, 99]
    k = 3
    s = Solution()
    print(s.rotate(nums, k))
