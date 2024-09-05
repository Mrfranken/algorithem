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
            add2 = k % 10
            tmp_sum = add1 + add2 + carry
            carry = 1 if tmp_sum >= 10 else 0
            res.append(tmp_sum % 10)
            p -= 1
            k = k // 10
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    num = [2, 7, 4]
    k = 181
    num = [2, 1, 5]
    k = 806
    print(s.addToArrayForm(num, k))
