class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        https://leetcode.cn/problems/assign-cookies/description/
        8.13 双指针 贪心
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        while j < len(s):
            if s[j] >= g[i]:
                i += 1
                j += 1
                if i == len(g):
                    break
            else:
                j += 1
        return i


if __name__ == '__main__':
    c = Solution()
    g = [1, 2]
    s = [1, 2, 3]
    print(c.findContentChildren(g, s))
