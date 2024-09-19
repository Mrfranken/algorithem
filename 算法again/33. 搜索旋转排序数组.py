class Solution(object):
    """
    https://leetcode.cn/problems/search-in-rotated-sorted-array/solutions/221747/pythonjs-er-fen-fa-33-sou-suo-xuan-zhuan-pai-xu-sh/?envType=study-plan-v2&envId=top-100-liked

    二分法
    1. 如果mid值大于left，那说明当前序列要么是升序，要么mid在左半部分的升序
        然后如果target在left和mid之间，则right 收缩到mid
           如果不在，那说明target大于mid，则右移left到mid + 1
    2. 如果mid值大于left，那说明mid一定在序列的右半侧
        然后如果target在mid和right之间，则右移left到mid +1
           如果不在，则左移right到mid
    """

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[left]:  # 一定在左半部分
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:  # 一定在右半部分
                if nums[mid + 1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return left if nums[left] == 0 else -1


if __name__ == '__main__':
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(s.search(nums, 4))
