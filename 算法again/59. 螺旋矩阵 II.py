class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        numbers = list(range(1, n ** 2 + 1))
        arrays = [[None] * n for _ in range(n)]

        top, bottom = 0, n - 1
        left, right = 0, n - 1
        index = 0
        while True:
            for i in range(left, right + 1):
                arrays[top][i] = numbers[index]
                index += 1
            top += 1

            if top > bottom:
                break

            for i in range(top, bottom + 1):
                arrays[i][right] = numbers[index]
                index += 1
            right -= 1

            if right < left:
                break

            for i in range(right, left - 1, -1):
                arrays[bottom][i] = numbers[index]
                index += 1
            bottom -= 1

            if bottom < top:
                break

            for i in range(bottom, top - 1, -1):
                arrays[i][left] = numbers[index]
                index += 1
            left += 1

            if left > right:
                break
        return arrays


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
