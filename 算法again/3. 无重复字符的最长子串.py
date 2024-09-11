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
            cur_length = index + 1
            while letter in window:
                window.remove(s[left])
                left += 1
            window.add(letter)
            ans = max(ans, len(window))
        return ans