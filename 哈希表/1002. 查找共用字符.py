class Solution(object):
    """
    https://leetcode.cn/problems/find-common-characters/description/
    哈希表

    解题：根据出现字母次数最小的字母返回结果
    """
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        l = []
        res = []
        for word in words:
            d = {}
            for item in word:
                d[item] = d.get(item, 0) + 1
            l.append(d)

        word0 = words[0]
        for letter in set(word0):
            if_all_contain = []
            for word in words[1:]:
                if_all_contain.append(letter in word)

            if all(if_all_contain):
                num = min([d[letter] for d in l])
                res.extend([letter] * num)
        return res


if __name__ == '__main__':
    words = ["bella", "label", "roller"]
    s = Solution()
    print(s.commonChars(words))
