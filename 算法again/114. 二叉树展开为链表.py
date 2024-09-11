# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """
    二叉树

    题解：
    1. 先前序遍历
    2. 然后将所有的node连接起来，left为None，right为下一个Node
    """
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.res = []
        self._pre_order(root)
        dummy = TreeNode()
        tmp = dummy
        for index, node in enumerate(self.res):
            tmp.left = None
            tmp.right = node
            tmp = node
        return dummy.right

    def _pre_order(self, root):
        if not root:
            return None

        self.res.append(root)
        self._pre_order(root.left)
        self._pre_order(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # root.left.right.right = TreeNode(15)
    # root.right.right = TreeNode(7)
    # root.right.right = TreeNode(7)
    print(Solution().flatten(root))
