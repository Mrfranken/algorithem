# class Solution(object):
#     def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#         start = 0
#         p = sorted(p)
#         k = len(p)
#         child_str = ''
#         res = []
#         for index, letter in enumerate(s):
#             child_str += letter
#             if len(child_str) == k:
#                 tmp = sorted(child_str)
#                 if tmp == p:
#                     res.append(start)
#                 child_str = child_str[1:]
#                 start += 1
#         return res


from string import ascii_lowercase


class Solution:
    def findAnagrams(self, s, p):
        ret = []
        k_dict = {}.fromkeys(ascii_lowercase, 0)
        for i in p:
            k_dict[i] += 1
        tmp = {}.fromkeys(ascii_lowercase, 0)
        left = right = 0
        while right < len(s):
            tmp[s[right]] += 1
            if tmp == k_dict:
                ret.append(left)
            if right - left + 1 == len(p):
                tmp[s[left]] -= 1
                left += 1
            right += 1
        return ret


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    # s = "abab"
    # p = "ab"
    so = Solution()
    print(so.findAnagrams(s, p))
