class Solution(object):
    """
    https://leetcode.cn/problems/backspace-string-compare/description/
    栈
    """
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        t_list = list(t)

        return self.backspace(s) == self.backspace(t)

    def backspace(self, s):
        stack = []
        for index in range(len(s)):
            symbol = s[index]
            if symbol != "#":
                stack.append(symbol)
            elif len(stack) > 0:
                stack.pop()
        return "".join(stack)