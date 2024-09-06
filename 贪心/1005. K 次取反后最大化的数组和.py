class Solution(object):

    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/solutions/1135780/dai-ma-sui-xiang-lu-dai-ni-xue-tou-tan-x-f4rq/
        8.13 贪心
        """

        sorted_nums = sorted(nums, key=abs, reverse=True)

        for index, num in enumerate(sorted_nums):
            if k > 0 and num < 0:
                sorted_nums[index] *= -1
                k -= 1

        if k > 0:
            sorted_nums[-1] = sorted_nums[-1] * (-1) ** k
        return sum(sorted_nums)


if __name__ == '__main__':
    s = Solution()
    nums = [4, 2, 3]
    k = 1
    nums = [3, -1, 0, 2]
    k = 3
    nums = [2, -3, -1, 5, -4]
    k = 2
    print(s.largestSumAfterKNegations(nums, k))
