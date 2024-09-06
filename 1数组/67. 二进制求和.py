class Solution(object):

    # def binary_sum(self, a, b):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        p1 = len(a) - 1
        p2 = len(b) - 1
        carry = 0
        while p1 >= 0 or p2 >= 0 or carry > 0:
            add1 = int(a[p1]) if p1 >= 0 else 0
            add2 = int(b[p2]) if p2 >= 0 else 0
            sum_value = add1 + add2 + carry
            value = sum_value % 2
            carry = sum_value // 2
            res.append(value)
            p1 -= 1
            p2 -= 1
        return ''.join([str(item) for item in res[::-1]])


if __name__ == '__main__':
    s = Solution()
    a = "1010"
    b = "1011"
    print(s.addBinary(a, b))
