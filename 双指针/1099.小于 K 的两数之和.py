class Solution:
    def twoSumLessThanK(self, numbers, K):
        numbers.sort()

        left, right = 0, len(numbers) - 1
        max_target = 0
        while left < right:
            if numbers[left] + numbers[right] >= K:
                right -= 1
            else:
                max_target = max(max_target, numbers[left] + numbers[right])
                left += 1
        return max_target
