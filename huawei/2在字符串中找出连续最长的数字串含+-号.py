import re
from typing import List


class Solution:
    """
    https://www.nowcoder.com/practice/1624bc35a45c42c0bc17d17fa0cba788
    """

    def search_max_nums_string(self, s: str):
        s = s.strip()
        pattern = "[-+]?\d+(\.\d+)?"
        max_string = ""
        for i in range(len(s)):
            sub_string = s[i:]
            result = re.search(pattern, sub_string)
            if result:
                tmp = result.group(0)
                if len(tmp) >= len(max_string):
                    max_string = tmp
        return max_string



        # # write code here
        # window_sum = sum(num[:size])
        # tmp = window_sum
        # for move_num in range(size, len(num)):
        #     window_sum = window_sum + num[move_num] - num[move_num - size]
        #     tmp = max(tmp, window_sum)
        # return tmp


if __name__ == '__main__':
    s = Solution()
    result = s.search_max_nums_string("1234567890abcd9.+12345.678.9ed")
    print(result)
