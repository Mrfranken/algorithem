class Solution(object):
    """
    https://leetcode.cn/problems/remove-element/description/
    """

    def removeElement(self, nums, val):
        a, b = 0, 0
        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1
        return b


if __name__ == '__main__':
    nums = [3, 2, 2, 3, 5, 2, 7]
    val = 2
    s = Solution()
    print(s.removeElement(nums, val))
