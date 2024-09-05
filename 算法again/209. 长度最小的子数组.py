from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        min_length = float('+inf')
        sum_nums = 0
        p = 0
        for index, num in enumerate(nums):
            sum_nums += num
            while sum_nums >= target:
                min_length = min(min_length, index - p + 1)
                sum_nums = sum_nums - nums[p]
                p += 1
        return min_length


if __name__ == '__main__':
    s = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(s.minSubArrayLen(target, nums))
