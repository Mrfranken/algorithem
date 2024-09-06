class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums) - 1
        res = [None, None]
        while left < right:
            if nums[left + 1] < nums[left]:
                res[0] = left
            else:
                left = left + 1
            if nums[right - 1] > nums[right]:
                res[1] = right
            else:
                right = right - 1
            if len(res) == 2 and None not in res:
                break
        res[0] = left
        res[1] = right
        return res[1] - res[0] + 1 if left != right else 0


if __name__ == '__main__':
    s = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    nums = [1, 2, 3, 4]
    nums = [1]
    nums = [1, 2, 3, 3, 3]
    print(s.findUnsortedSubarray(nums))
