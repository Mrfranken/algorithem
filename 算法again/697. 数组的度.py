class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for index, num in enumerate(nums):
            if num in d:
                d[num] = d.get(num, 0) + 1
            else:
                d[num] = 1
        c_list = sorted(d.items(), key=lambda item: item[-1], reverse=True)

        max_count = c_list[0][1]

        count = 0
        res = []

        outcome = float("+inf")
        for item in c_list:
            if item[1] == max_count:

                count = 0
                res = []
                for index, num in enumerate(nums):
                    if num == item[0]:
                        count += 1
                        res.append(index)
                    if count == c_list[0][1]:
                        outcome = min(res[-1] - res[0] + 1, outcome)
        return outcome


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1, 4, 2]
    nums = [1, 2, 2, 3, 1]
    s = Solution()
    print(s.findShortestSubArray(nums))
