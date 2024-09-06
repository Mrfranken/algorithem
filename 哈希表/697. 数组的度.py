class Solution(object):
    """
    哈希表
    """

    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, counter = {}, {}
        for index, num in enumerate(nums):
            l = s.get(num, [])
            l.append(index)
            s[num] = l

            counter[num] = counter.get(num, 0) + 1

        c_list = sorted(counter.items(), key=lambda item: item[-1], reverse=True)
        max_counter = c_list[0][1]
        res = len(nums)
        for c in c_list:
            if c[1] == max_counter:
                res = min(res, s[c[0]][-1] - s[c[0]][0] + 1)

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2, 3, 1, 4, 2]
    nums = [1, 2, 2, 3, 1]
    print(s.findShortestSubArray(nums))
