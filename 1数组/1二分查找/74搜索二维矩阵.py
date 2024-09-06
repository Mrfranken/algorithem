matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = []
        for item in matrix:
            m.extend(item)

        left, right = 0, len(m) - 1
        while left <= right:
            mid = (left + right) // 2
            if m[mid] < target:
                left = mid + 1
            elif m[mid] > target:
                right = mid - 1
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    s.searchMatrix(matrix, target)
