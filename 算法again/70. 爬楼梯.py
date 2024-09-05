class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        f = [1, 2] + [0] * (n - 2)
        for i in range(2, n):
            f[i] = f[i - 1] + f[i - 2]
        return f[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
