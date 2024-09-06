class Solution(object):
    """
    https://leetcode.cn/problems/isomorphic-strings/
    https://leetcode.cn/problems/isomorphic-strings/solutions/1645867/by-jyd-i4wt/
    使用hash表建立映射关系
    """

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        length = len(s)
        s2t = {}
        t2s = {}
        for i in range(length):
            si = s[i]
            ti = t[i]
            if (si in s2t and s2t[si] != ti) or (ti in t2s and t2s[ti] != si):
                return False
            s2t[si] = ti
            t2s[ti] = si
        return True


if __name__ == '__main__':
    s = "egg"
    t = "add"
    print(Solution().isIsomorphic(s, t))
