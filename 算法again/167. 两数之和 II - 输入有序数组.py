class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        https://leetcode.cn/problems/two-sum/solutions/2326193/dong-hua-cong-liang-shu-zhi-he-zhong-wo-0yvmj/
        数组 哈希表
        """
        d = {}
        for i, num in enumerate(numbers):
            if target - num in d:
                if i > d[target - num]:
                    return [d[target - num] + 1, i + 1]

            d[num] = i
