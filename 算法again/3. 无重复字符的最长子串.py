class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        left = 0
        ans = 0
        for index, letter in enumerate(s):
            while letter in window:
                window.remove(s[left])
                left += 1
            window.add(letter)
            ans = max(ans, len(window))
        return ans


if __name__ == '__main__':
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
