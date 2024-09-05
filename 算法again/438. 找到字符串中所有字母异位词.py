class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l = len(p)
        pd = {}
        for letter in p:
            pd[letter] = pd.get(letter, 0) + 1

        tmp = {}
        left = 0
        result = []
        for right, letter in enumerate(s):
            tmp[letter] = tmp.get(letter, 0) + 1

            if tmp == pd:
                result.append(left)

            if right - left + 1 == l:
                tmp[s[left]] -= 1

                if tmp[s[left]] == 0:
                    del tmp[s[left]]

                left += 1
        return result


if __name__ == '__main__':
    so = Solution()
    s = "cbaebabacd"
    p = "abc"
    print(so.findAnagrams(s, p))
