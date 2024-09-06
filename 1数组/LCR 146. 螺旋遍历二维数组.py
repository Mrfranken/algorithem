class Solution(object):
    def spiralArray(self, array):
        """
        :type array: List[List[int]]
        :rtype: List[int]
        """
        right, bottom = len(array[0]) - 1, len(array) - 1
        left, top = 0, 0
        res = []
        if not array:
            return res
        while True:
            for i in range(left, right + 1):
                res.append(array[top][i])
            top += 1

            if top > bottom:
                break
            for i in range(top, bottom + 1):
                res.append(array[i][right])
            right -= 1

            if right < left:
                break
            for i in range(right, left - 1, -1):
                res.append(array[bottom][i])
            bottom -= 1

            if bottom < top:
                break
            for i in range(bottom, top - 1, -1):
                res.append(array[i][left])
            left += 1

            if left > right:
                break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.spiralArray([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
