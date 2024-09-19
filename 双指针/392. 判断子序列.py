class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        fast, slow = 0, 0
        while slow < len(s) and fast < len(t):
            slow_letter = s[slow]
            fast_letter = t[fast]
            if slow_letter == fast_letter:
                fast += 1
                slow += 1
            else:
                fast += 1

        if slow < len(s):
            return False
        return True
