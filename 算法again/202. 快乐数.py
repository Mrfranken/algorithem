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
            num_sum = 0
            s.add(n)
            for i in str(n):
                num_sum += int(i) ** 2
            if num_sum == 1:
                return True
            else:
                n = num_sum
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))