class Solution(object):
    def groupAnagrams(self, strs):
        """
        https://leetcode.cn/problems/group-anagrams/solutions/2718519/ha-xi-biao-fen-zu-jian-ji-xie-fa-pythonj-1ukv/?envType=study-plan-v2&envId=top-100-liked
        哈希表
        """
        d = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            l = d.get(sorted_str, [])
            l.append(s)
            d[sorted_str] = l
        return [v for _, v in d.items()]