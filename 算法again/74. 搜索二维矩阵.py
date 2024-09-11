class Solution(object):
    """
    题解： 从矩阵的左下角开始搜索
    1. 当target大于当前点，向右走
    2. 当target小于当前点，向上走
    """

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = len(matrix) - 1  # 0 i
        j = 0  # 0 len(matrix[0])

        while i >= 0 and j < len(matrix[0]):
            num = matrix[i][j]
            if num == target:
                return True
            elif target > num:
                j += 1
            elif target < num:
                i -= 1
        return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    s = Solution()
    print(s.searchMatrix(matrix, target))
