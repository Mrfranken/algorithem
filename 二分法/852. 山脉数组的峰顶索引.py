class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        https://leetcode.cn/problems/peak-index-in-a-mountain-array/description/
        二分法
        """
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid - 1]:
                left = left - 1
            else:
                right = right + 1


if __name__ == '__main__':
    s = Solution()
    arr = [0, 3, 4, 5, 10, 5, 2]
    print(s.peakIndexInMountainArray(arr))
