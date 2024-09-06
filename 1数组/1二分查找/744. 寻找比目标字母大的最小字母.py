class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        https://leetcode.cn/problems/find-smallest-letter-greater-than-target/description/
        """

        def search_target(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        start = search_target(letters, target)

        # if start == len(letters) and letters[-1] != target:
        #     return letters[0]
        # if start == 0 and letters[start] == target:
        #     return letters[1]
        # return letters[start]
        return letters[start % len(letters)]


if __name__ == '__main__':
    s = Solution()
    letters = ["c", "f", "j"]
    # letters = ["x", "x", "y", "y"]
    # target = "a"
    target = "a"
    target = "c"
    # target = "h"
    print(s.nextGreatestLetter(letters, target))
