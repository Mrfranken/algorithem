# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-100-liked

    题解：二叉搜索树按照中序遍历 排除所有val为None的节点，用实例属性res保存下来，然后获取index为k-1的值
    """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = []
        self._middle_order(root)
        return self.res[k - 1]

    def _middle_order(self, root):
        if not root:
            return None

        self._middle_order(root.left)
        if root.val is not None:
            self.res.append(root.val)
        self._middle_order(root.right)
