class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # slow, fast = 0, 0
        # count = 0
        # if nums == [0]:
        #     return 0
        #
        # while fast < len(nums):
        #     if nums[fast] == nums[slow] and nums[fast] == 1:
        #         fast += 1
        #     else:
        #         count = max(count, fast - slow)
        #         slow = fast
        #         if nums[slow] == 0:
        #             slow += 1
        #             fast += 1
        # return max(count, fast - slow)
        count = 0
        for i, num in enumerate(nums):
            if num == 0:
                index = i
            else:
                count = max(count, i - index)
        return count


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 0, 1]
    # nums = [1, 1, 0, 1, 1, 1]
    # nums = [1]
    # nums = [0, 0]
    s = Solution()
    print(s.findMaxConsecutiveOnes(nums))
