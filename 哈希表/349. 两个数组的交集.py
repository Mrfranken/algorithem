class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        https://leetcode.cn/problems/intersection-of-two-arrays/description/
        哈希表
        """
        d = {}
        res = []
        for _, num in enumerate(nums1):
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        for _, num in enumerate(nums2):
            if num in d and num not in res:
                res.append(num)
        return res


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(s.intersection(nums1, nums2))
