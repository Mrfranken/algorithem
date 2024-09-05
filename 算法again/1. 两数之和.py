class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        https://leetcode.cn/problems/two-sum/solutions/2326193/dong-hua-cong-liang-shu-zhi-he-zhong-wo-0yvmj/
        数组 哈希表
        """
        res = {}
        for i in range(len(nums)):
            if target - nums[i] in res:
                return [res[target - nums[i]], i]
            res[nums[i]] = i

