class Solution(object):
    """
    https://leetcode.cn/problems/longest-palindrome/description/
    最长回文串

    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for item in s:
            d[item] = d.get(item, 0) + 1

        count = 0
        centre = 0
        odd_list = []
        for k, v in d.items():
            if v % 2 == 0:
                count += v
            else:
                centre = 1
                count += (v - 1)
        return count + centre


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("bb"))
