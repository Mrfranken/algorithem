class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        p = len(num) - 1
        carry = 0
        res = []
        while p >= 0 or k != 0 or carry != 0:
            add1 = num[p] if p >= 0 else 0
            add2 = k % 10 if k != 0 else 0
            sum_value = add1 + add2 + carry
            carry = sum_value // 10
            value = sum_value % 10
            res.append(value)
            p -= 1
            k = k // 10
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    num = [2, 1, 5]
    k = 806
    print(s.addToArrayForm(num, k))
