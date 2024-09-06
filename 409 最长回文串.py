class Solution(object):
    def longestPalindrome(self, s):
        """
        首先统计每个字母出现的频次，如果是偶数个那他们放在两边肯定能对称，
        如果是奇数个有两种可能：
        1）放在正中间可以对称，
        2）删掉一个也就变成了偶数个。
        因此统计完之后，把第一个奇数放在中间，剩下的所有奇数都减去1
        """
        d = {}
        for letter in s:
            if letter in d:
                d[letter] = d[letter] + 1
            else:
                d[letter] = 1

        # d = {v: k for k, v in d.items()}
        counter_list = list(d.values())
        num = 0
        flag = False
        for counter in counter_list:
            if counter % 2 == 0:
                num += counter
            else:
                if not flag:
                    num += counter
                else:
                    num = num + counter - 1
        return num


if __name__ == '__main__':
    solu = Solution()
    v = solu.longestPalindrome('abccccdd')
    print(v)
