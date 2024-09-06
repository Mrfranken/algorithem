class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        max_r = arr[-1]

        res = [0] * len(arr)
        for i in range(n - 2, -1, -1):
            tmp = arr[i]
            max_r = max(tmp, max_r)
            res[i] = max_r
        del res[0]
        res[-1] = arr[-1]
        res.append(-1)
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [17, 18, 5, 4, 6, 1]
    print(s.replaceElements(arr))
