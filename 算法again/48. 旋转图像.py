class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        p1, p2 = 0, len(matrix) - 1
        while p1 < p2:
            add = 0
            while add < p2 - p1:
                bottom_left = matrix[p2 - add][p1]
                matrix[p2 - add][p1] = matrix[p2][p2 - add]

                matrix[p2][p2 - add] = matrix[p1 + add][p2]

                matrix[p1 + add][p2] = matrix[p1][p1 + add]

                matrix[p1][p1 + add] = bottom_left

                add += 1
            p1 += 1
            p2 -= 1

        return matrix
