class Solution(object):
    """
    https://leetcode.cn/problems/check-array-formation-through-concatenation/description/
    哈希表
    """
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        pies = {}
        # for item in pieces:
            # if len(item) > 1:
            #     item = [int(''.join([str(num) for num in item]))]
            # pies[item] = pies.get(item[0], 0) + 1

        for index, piece in enumerate(pieces):
            pies[piece[0]] = index

        index = 0
        while index < len(arr):
            item = arr[index]
            if item not in pies:
                return False
            child_list = pieces[pies[item]]
            if arr[index: index+len(child_list)] != child_list:
                return False
            index += len(child_list)
        return True


if __name__ == '__main__':
    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]
    print(Solution().canFormArray(arr, pieces))
