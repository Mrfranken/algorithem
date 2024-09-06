class Solution(object):
    """
    https://leetcode.cn/problems/add-to-array-form-of-integer/solutions/1081156/fu-xue-ming-zhu-zong-jie-qiu-jia-fa-ti-m-s2ac/
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        p = len(digits) - 1
        add2_list = [1]
        p2 = 0
        carry = 0
        res = []

        while p >= 0 or p2 >= 0 or carry > 0:
            add1 = digits[p] if p >= 0 else 0
            add2 = add2_list[p2] if p2 >= 0 else 0
            sum_value = add1 + add2 + carry
            value = sum_value % 10
            carry = sum_value // 10
            res.append(value)
            p -= 1
            p2 -= 1
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    digits = [1, 2, 3]
    digits = [4, 3, 2, 1]
    digits = [9]
    print(s.plusOne(digits))
