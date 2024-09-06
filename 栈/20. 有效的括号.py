class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        https://leetcode.cn/problems/valid-parentheses/description/
        栈
        """
        if len(s) == 1:
            return False
        stack = []
        for item in s:
            if item == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif item == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif item == "}" and stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(item)
        return not stack