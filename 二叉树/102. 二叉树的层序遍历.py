from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    理解deque的使用
    层序遍历时，每次清空queue并保存起来便能获得按层序遍历的值
    """
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return None

        queue = deque([root])
        res = []
        while queue:

            vals = []

            for _ in range(len(queue)):
                node = queue.popleft()
                vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(vals)
        return res
