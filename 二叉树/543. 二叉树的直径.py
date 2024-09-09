from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    二叉树
    最长路径实际就是 左子树路径 右子树路径 和 左+右子树路径（经过根节点的路径） 的对比
    题解 https://leetcode.cn/problems/diameter-of-binary-tree/solutions/141445/liang-chong-si-lu-shi-yong-quan-ju-bian-liang-yu-b
    """

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, route = self._preorderTraversal(root)
        return route

    def _preorderTraversal(self, root):
        if not root:
            return (0, 0)

        left_depth, left_route = self._preorderTraversal(root.left)
        right_depth, right_route = self._preorderTraversal(root.right)
        depth = max(left_depth, right_depth) + 1
        route = max(left_route, right_route, left_depth + right_depth)
        return (depth, route)
