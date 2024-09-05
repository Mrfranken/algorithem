class Solution(object):
    """
    https://leetcode.cn/problems/isomorphic-strings/
    https://leetcode.cn/problems/isomorphic-strings/solutions/1645867/by-jyd-i4wt/
    使用hash表建立映射关系
    """

    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        si = {}
        ti = {}

        for i in range(len(s)):
            s_value = s[i]
            t_value = t[i]

            if (s_value in si and si[s_value] != t_value) or (t_value in ti and ti[t_value] != s_value):
                return False

            si[s_value] = t_value
            ti[t_value] = s_value
        return True


if __name__ == '__main__':
    s = "egg"
    t = "bar"
    solution = Solution()
    print(solution.isIsomorphic(s, t))
