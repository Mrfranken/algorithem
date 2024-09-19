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
                left += 1

            if nums[right - 1] > nums[right]:
                res[1] = right
            else:
                right -= 1

            if len(res) == 2 and None not in res:
                break

        if res[1] is None or res[0] is None:
            return 0
        else:
            return res[1] - res[0] + 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    nums = [1, 3, 2, 3, 3]
    nums = [1, 2, 3, 3, 3]
    nums = [2, 6, 4, 8, 10, 9, 15]
    nums = [1, 3, 2, 2, 2]
    print(s.findUnsortedSubarray(nums))
