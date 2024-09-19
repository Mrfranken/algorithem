class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for letter in s:
            d[letter] = d.get(letter, 0) + 1

        for index, letter in enumerate(s):
            if d[letter] == 1:
                return index
        return -1



if __name__ == '__main__':
    s = "loveleetcode"
    print(Solution().firstUniqChar(s))