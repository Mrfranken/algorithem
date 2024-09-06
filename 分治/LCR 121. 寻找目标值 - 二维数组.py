class Solution(object):
    """
    https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solutions/95306/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/
    """

    def findTargetIn2DPlants(self, plants, target):
        """
        :type plants: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left_i = len(plants) - 1
        left_j = 0  # 0<= left_j < len(plants[-1])

        while left_i >= 0 and left_j < len(plants[-1]):
            if plants[left_i][left_j] < target:
                left_j += 1
            elif plants[left_i][left_j] > target:
                left_i -= 1
            else:
                return True
        return False



if __name__ == '__main__':
    s = Solution()
    plants = [[2, 3, 6, 8], [4, 5, 8, 9], [5, 9, 10, 12]]
    plants = [[-5]]
    target = 8
    target = -5
    print(s.findTargetIn2DPlants(plants, target))
