class Solution(object):
    """
    双指针 中心扩散法
    如果回文串的长度为奇数，则它有一个中心字符；        aba
    如果回文串的长度为偶数，则可以认为它有两个中心字符。  abba
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def palindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        res = ''
        for i in range(len(s)):
            sub1 = palindrome(s, i, i)
            sub2 = palindrome(s, i, i + 1)
            res = sub1 if len(sub1) > len(res) else res
            res = sub2 if len(sub2) > len(res) else res
        return res


if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))
