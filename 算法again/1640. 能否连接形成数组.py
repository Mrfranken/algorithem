class Solution(object):
    """
    https://leetcode.cn/problems/check-array-formation-through-concatenation/description/
    哈希表
    """

    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        d = {}
        for index, piece in enumerate(pieces):
            d[piece[0]] = len(piece)

        index = 0
        while index < len(arr):
            if arr[index] not in d:
                return False

            tmp = index + d[arr[index]]
            if arr[index: tmp] not in pieces:
                return False

            index = tmp
        return True


if __name__ == '__main__':
    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]
    s = Solution()
    print(s.canFormArray(arr, pieces))
