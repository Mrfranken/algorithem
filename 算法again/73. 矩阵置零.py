class Solution(object):
    """
    给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
    """

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        row = len(matrix)
        col = len(matrix[0])
        status = [[False] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    status[i][j] = True

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0 and status[i][j]:
                    for index in range(col):
                        matrix[i][index] = 0

                    for index in range(row):
                        matrix[index][j] = 0
        return matrix