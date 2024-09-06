class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = []
        left = 0
        ans = 0
        for index, letter in enumerate(s):
            while letter in window:
                # window.remove(s[left])
                del window[0]
                left += 1
            window.append(letter)
            ans = max(ans, len(window))
        return ans


if __name__ == '__main__':
    so = Solution()
    s = "abcdbcbb"
    print(so.lengthOfLongestSubstring(s))
