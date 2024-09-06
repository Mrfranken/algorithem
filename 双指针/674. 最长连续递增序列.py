class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = 0, 0
        res = []
        if len(nums) == 1:
            return 1
        while fast < len(nums):
            try:
                value = nums[fast + 1]
            except:
                break
            if slow >= fast or nums[fast] < value:
                fast += 1
                res.append(fast - slow + 1)
            else:
                slow = fast + 1
        return max(res)


if __name__ == '__main__':
    s = Solution()
    nums = [1]
    print(s.findLengthOfLCIS(nums))
