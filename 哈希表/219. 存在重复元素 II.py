class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for index, num in enumerate(nums):
            value = d.get(num, [])
            value.append(index)
            d[num] = value

        for _, v in d.items():
            if len(v) >= 2:
                i = 0
                while i <= len(v) - 2:
                    if abs(v[i] - v[i + 1]) <= k:
                        return True
                    i += 1
        return False


if __name__ == '__main__':
    nums = [1, 0, 1, 1]
    k = 1
    print(Solution().containsNearbyDuplicate(nums, k))
