class Solution(object):
    """
    https://leetcode.cn/problems/pascals-triangle/solutions/2784222/jian-dan-ti-jian-dan-zuo-pythonjavaccgoj-z596/
    https://leetcode.cn/problems/pascals-triangle/description/
    动态规划
    杨辉三角
    """
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        c = [[1] * i for i in range(1, numRows + 1)]
        for i in range(2, numRows):
            # i = len(i) - 1
            for j in range(1, i):
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
        return c


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
