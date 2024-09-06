class Solution(object):
    """
    https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/description/
    栈
    """
    def __init__(self):
        self.stack = []

    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        for item in s:
            if not self.stack:
                self.stack.append(item)
                continue
            if item == self.stack[-1]:
                self.stack.pop()
            else:
                self.stack.append(item)

        return ''.join(self.stack)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates('abbaca'))
