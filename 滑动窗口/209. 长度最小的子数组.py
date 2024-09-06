class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = float("inf")
        sum_value = 0
        start = 0
        for end, num in enumerate(nums):
            sum_value += num

            while sum_value >= target:
                min_len = min(min_len, end - start + 1)
                sum_value = sum_value - nums[start]
                start += 1

        if min_len == float("inf"):
            return 0

        return min_len


if __name__ == '__main__':
    s = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(s.minSubArrayLen(target, nums))
