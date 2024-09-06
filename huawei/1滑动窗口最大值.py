#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @param size int整型
# @return int整型一维数组
#
from typing import List


class Solution:
    """
    https://www.nowcoder.com/practice/1624bc35a45c42c0bc17d17fa0cba788
    """

    def maxInWindows(self, num: List[int], size: int) -> List[int]:
        # write code here
        window_sum = sum(num[:size])
        tmp = window_sum
        for move_num in range(size, len(num)):
            window_sum = window_sum + num[move_num] - num[move_num - size]
            tmp = max(tmp, window_sum)
        return tmp




if __name__ == '__main__':
    s = Solution()
    s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3)
