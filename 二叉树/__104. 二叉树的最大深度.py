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

    def max_depth_used_iterable(self, root):
        """
        迭代法
        """
        max_depth = 1
        res = []
        stack = [(root, max_depth)]
        while stack:
            node, depth = stack.pop()
            res.append(node.val)
            max_depth = max(max_depth, depth)

            if node.right:
                stack.append((node.right, max_depth + 1))

            if node.left:
                stack.append((node.left, max_depth + 1))
        return max_depth


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxDepth(root))
    print(Solution().max_depth_used_iterable(root))
