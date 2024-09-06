from typing import List


class Solution(object):
    def threeSum(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        https://leetcode.cn/problems/3sum/description/
        """
        nums.sort()  # i < j < k  => i < left < right
        res = []
        for index, i in enumerate(nums[:-2]):

            if index > 0 and i == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            target = 0 - i
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([i, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, -1, 0, 1, 2, -4]))
