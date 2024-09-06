# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self._inorderTraversal(root)
        return self.res

    def _inorderTraversal(self, root):
        if not root:
            return None
        self._inorderTraversal(root.left)
        self.res.append(root.val)
        self._inorderTraversal(root.right)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    c1_right = TreeNode(2)
    c2_left = TreeNode(3)
    root.right = c1_right
    c1_right.left = c2_left
    print(s.inorderTraversal(root))
