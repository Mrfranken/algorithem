class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        start = 0
        sum_num = 0
        s = set()
        d = {}
        for end, num in enumerate(nums):
            sum_num += num
            while num in s:
                s.remove(nums[start])
                sum_num -= nums[start]
                start += 1

            s.add(num)
            if sum_num >= max_sum:
                max_sum = sum_num
        return max_sum


if __name__ == '__main__':
    nums = [4, 2, 4, 5, 6]
    s = Solution()
    print(s.maximumUniqueSubarray(nums))
