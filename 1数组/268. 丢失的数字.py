class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        for index, num in enumerate(range(len(nums))):
            if index != nums[index]:
                return index
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1]
    print(s.missingNumber(nums))
