class Solution(object):
    """
    遇到1走两步
    遇到0走一步
    """
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        length = len(bits)
        i = 0
        while i < length - 1:
            if bits[i] == 1:
                i += 2
            elif bits[i] == 0:
                i += 1

        if i == length:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    bits = [1, 0, 0]
    # bits = [1, 1, 1, 0]
    print(s.isOneBitCharacter(bits))
