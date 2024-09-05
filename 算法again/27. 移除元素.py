class Solution(object):
    def removeElement(self, nums, val):
        slow, fast = 0, len(nums) - 1
        while fast <= slow:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
