class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        https://leetcode.cn/problems/two-sum/solutions/2326193/dong-hua-cong-liang-shu-zhi-he-zhong-wo-0yvmj/
        数组 哈希表
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         https://leetcode.cn/problems/two-sum/solutions/2326193/dong-hua-cong-liang-shu-zhi-he-zhong-wo-0yvmj/
#         数组 哈希表
#         """
#         d = {}
#         for i, num in enumerate(nums):
#             if target - num in d:
#                 if i > d[target - num]:
#                     return [d[target - num], i]
#             d[num] = i


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    # nums = [3, 2, 4]
    target = 9
    print(s.twoSum(nums, target))
