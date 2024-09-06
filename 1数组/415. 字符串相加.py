class Solution(object):
    """
    https://leetcode.cn/problems/add-to-array-form-of-integer/solutions/1081156/fu-xue-ming-zhu-zong-jie-qiu-jia-fa-ti-m-s2ac/
    关键：
    1. 理解竖式加法
    2. while p1 >= 0 or p2 >= 0 or carry != 0 这行代码中每个条件缺一不可
    3. 如果是链表的话，可能涉及到先先翻转链表
        445. 两数相加 II
    """
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        res = []
        while p1 >= 0 or p2 >= 0 or carry != 0:
            add1 = int(num1[p1]) if p1 >= 0 else 0
            add2 = int(num2[p2]) if p2 >= 0 else 0
            sum_value = add1 + add2 + carry
            carry = sum_value // 10
            value = sum_value % 10
            res.append(value)
            p1 -= 1
            p2 -= 1
        return ''.join(str(num) for num in res[::-1])


if __name__ == '__main__':
    num1 = "1"
    num2 = "9"
    print(Solution().addStrings(num1, num2))
