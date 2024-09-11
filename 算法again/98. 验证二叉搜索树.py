# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    二叉搜索树的性质是中序遍历的所有值由小到大排列

    题解：采用中序编列，排除val是None的值。然后验证左右相邻的点，右值是否大于左值
    """

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = []
        self.middle_order(root)
        for i in range(1, len(self.res)):
            if self.res[i] < self.res[i - 1]:
                return False
        return True

    def middle_order(self, root):
        if not root:
            return None

        self.middle_order(root.left)
        if root.val is not None:
            self.res.append(root.val)
        self.middle_order(root.right)
