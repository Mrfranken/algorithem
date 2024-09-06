class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        value = sum(arr) % 3
        average = sum(arr) // 3
        if value != 0:
            return False
        sum_value = 0
        res = []
        for index, num in enumerate(arr):
            sum_value += num
            if sum_value == average:
                res.append(sum_value)
                sum_value = 0
                if len(res) == 2 and index != len(arr) - 1:
                    return True
        return False


if __name__ == '__main__':
    arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    s = Solution()
    print(s.canThreePartsEqualSum(arr))
