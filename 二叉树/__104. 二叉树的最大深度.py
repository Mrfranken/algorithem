# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self._preorderTraversal(root)

    def _preorderTraversal(self, root):
        if not root:
            return 0
        left = self._preorderTraversal(root.left)
        right = self._preorderTraversal(root.right)
        return 1 + max(left, right)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxDepth(root))
