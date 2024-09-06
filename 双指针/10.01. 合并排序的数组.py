class Solution(object):
    def merge(self, A, m, B, n):
        """
        这里 a >= 0 非常有必要
        """
        point = m + n - 1
        a = m - 1
        b = len(B) - 1
        while b >= 0:
            if A[a] <= B[b] and a >= 0:
                A[point] = A[a]
                a -= 1
            else:
                A[point] = B[b]
                b -= 1
            point -= 1
        return A


if __name__ == '__main__':
    s = Solution()
    # A = [1, 2, 3, 0, 0, 0]
    # m = 3
    # B = [2, 5, 6]
    # n = 3
    A = [0]
    m = 0
    B = [1]
    n = 1
    print(s.merge(A, m, B, n))
