class Solution(object):
    """
    https://leetcode.cn/problems/island-perimeter/description/
    https://leetcode.cn/problems/island-perimeter/solutions/231191/zhi-jie-bian-li-dai-ma-qing-xi-by-tian-dao-yao-xin/
    只判断上方和左侧是否有重合
    """

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        res -= 2

                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        res -= 2
        return res


if __name__ == '__main__':
    s = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(s.islandPerimeter(grid))
