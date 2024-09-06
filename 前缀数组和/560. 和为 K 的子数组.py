class Solution(object):
    """
    有几种 i、j 的组合，使得从第 i 到 j 项的子数组和等于 k。
    ↓ ↓ ↓ 转化为 ↓ ↓ ↓ 有几种 i、j 的组合，满足 prefixSum[j] - prefixSum[i - 1] == k
    这里给我整明白了
    我们在梦开始的地方-- 两数之和 中，求解的是： 有几种 i、j 的组合，满足 nums[i] + nums[j] == target
    """
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        tmp = [0] * (len(nums) + 1)
        for index in range(len(nums)):
            tmp[index + 1] = tmp[index] + nums[index]

        d = {}
        count = 0
        for index, num in enumerate(tmp):
            if tmp[index] - k in d:
                count += d[tmp[index] - k]
            d[num] = d.get(num, 0) + 1
        return count


if __name__ == '__main__':
    nums = [1, 1, -1, 1, -1]
    k = 1
    s = Solution()
    print(s.subarraySum(nums, k))
