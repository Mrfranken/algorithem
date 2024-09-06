class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        left = 0
        right = len(arr) - 1
        while left + 1 < len(arr) and arr[left + 1] > arr[left]:
            left += 1
        while right > 0 and arr[right] < arr[right - 1]:
            right -= 1

        if left > 0 and right < len(arr) - 1 and left == right:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    arr = [0, 3, 2, 1]
    # arr = [3, 5, 5]
    arr = [2, 1]
    print(s.validMountainArray(arr))
