class Solution(object):
    def thirdMax(self, nums):

        nums.sort()

        if len(nums) <= 2:
            return nums[-1]

        count = 0
        max_num = float('+inf')
        for index in range(len(nums) - 1, -1, -1):
            num = nums[index]
            if num == max_num:
                continue
            max_num = min(max_num, num)
            count += 1
            if count >= 3:
                break
        return max_num if count == 3 else max(nums)


s = Solution()
nums = [2, 2, 3, 1]
nums = [3,2,1]
print(s.thirdMax(nums))
