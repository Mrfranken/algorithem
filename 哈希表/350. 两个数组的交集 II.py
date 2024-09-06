class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        https://leetcode.cn/problems/intersection-of-two-arrays-ii/description/
        哈希表
        """
        d = {}
        res = []

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        for _, num in enumerate(nums1):
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        for _, num in enumerate(nums2):
            if num in d and d[num] > 0:
                d[num] -= 1
                res.append(num)

        return res


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums1 = [4,9,5]
    nums2 = [2, 2]
    nums2 = [9,4,9,8,4]
    print(s.intersect(nums1, nums2))
