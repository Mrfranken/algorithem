class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()

        tmp = ''
        res = []

        slow = len(s) - 1
        fast = len(s) - 1

        while fast >= 0:
            while fast >= 0 and s[fast] != ' ':
                fast -= 1
            res.append(s[fast + 1: slow + 1])

            while s[fast] == " ":
                fast -= 1
            slow = fast

        return ' '.join(res)


if __name__ == '__main__':
    s = "a good   example "
    print(Solution().reverseWords(s))
