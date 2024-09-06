class Solution(object):
    """
    https://leetcode.cn/problems/maximum-average-subarray-i/
    """

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sub_list = []
        max_avg = float('-inf')
        sum_value = 0
        start = 0
        count = 0
        shrink = False
        for end, n in enumerate(nums):
            sum_value = sum_value + n
            index = end - start + 1
            if index == k:
                shrink = True
                max_avg = max(max_avg, sum_value / float(k))

            if shrink:
                sum_value -= nums[start]
                start += 1
                shrink = False
        return max_avg


if __name__ == '__main__':
    ums = [1, 12, -5, -6, 50, 3]
    ums = [-1]
    s = Solution()
    print(s.findMaxAverage(ums, 1))
