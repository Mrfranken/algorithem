class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            are = min(height[left], height[right]) * (right - left)
            max_area = max(are, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
