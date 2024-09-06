class Solution(object):
    """
    双指针
    """

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                del nums[slow]
            else:
                slow += 1
                fast += 1
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(s.removeDuplicates(nums))
