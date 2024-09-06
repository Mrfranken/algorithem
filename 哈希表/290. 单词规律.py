class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ")
        if len(pattern) != len(s):
            return False

        length = len(pattern)
        p2s = {}
        s2p = {}
        for i in range(length):
            si = pattern[i]
            ti = s[i]
            if (si in p2s and p2s[si] != ti) or (ti in s2p and s2p[ti] != si):
                return False
            p2s[si] = ti
            s2p[ti] = si
        return True
