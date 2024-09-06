class Solution(object):
    """
    https://leetcode.cn/problems/merge-sorted-array/description/

    """

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        point1 = m - 1
        point2 = n - 1
        point = m + len(nums2) - 1
        while point2 >= 0:
            if nums1[point1] >= nums2[point2] and point1 >= 0:  # 这里的point1>=0很有讲究
                nums1[point] = nums1[point1]
                point1 -= 1
            else:
                nums1[point] = nums2[point2]
                point2 -= 1
            point -= 1
        return nums1


if __name__ == '__main__':
    s = Solution()
    print(s.merge([2, 0], 1, [1], 1))
