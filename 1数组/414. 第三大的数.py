class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) <= 2:
            return nums[-1]
        tmp = float("+inf")
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == tmp:
                continue
            tmp = min(nums[i], tmp)
            count += 1
            if count == 3:
                break
        return tmp if count == 3 else max(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 3, 1]
    nums = [1, 1, 2]
    print(s.thirdMax(nums))
