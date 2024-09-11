class Solution(object):
    """
    贪心算法 动态规划
    """

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cover = 0
        count = 0
        if len(nums) <= 1:
            return 0
        for i in range(len(nums)):
            if cover >= i:
                cover = max(cover, i + nums[i])
                count += 1
                if cover >= len(nums) - 1:
                    return count


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    nums = [1, 2, 1, 1, 1]
    s = Solution()
    print(s.canJump(nums))
