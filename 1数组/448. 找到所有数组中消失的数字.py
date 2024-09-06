class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        for i in range(1, len(nums) + 1):
            if i != nums[i - 1] and i not in nums:
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(s.findDisappearedNumbers(nums))
