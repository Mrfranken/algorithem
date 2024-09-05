class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = 0
        for index, num in enumerate(nums):
            nums[index] = s + num
            s = nums[index]
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    print(s.runningSum(nums))
