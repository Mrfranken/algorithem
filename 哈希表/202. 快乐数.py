class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        题目中说了会 无限循环，那么也就是说求和的过程中，sum会重复出现

        https://leetcode.cn/problems/happy-number/description/
        """
        s = set()
        while n not in s:
            s.add(n)
            sum = 0
            for i in str(n):
                sum += int(i)**2
            if sum == 1:
                return True
            else:
                n = sum
        return False