class Solution(object):
    def countTarget(self, scores, target):
        """
        :type scores: List[int]
        :type target: int
        :rtype: int
        https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
        二分法
        """
        left, right = 0, len(scores) - 1
        while left <= right:
            mid = (left + right) // 2
            if scores[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if left > len(scores) - 1:
            return 0

        if scores[left] != target:
            return 0

        left, right = left, left
        # while left - 1 >= 0 and scores[left - 1] < target:
        #     left -= 1

        while right + 1 <= len(scores) - 1 and scores[right + 1] == target:
            right += 1

        return right - left + 1


if __name__ == '__main__':
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 11
    print(s.countTarget(nums, target))
