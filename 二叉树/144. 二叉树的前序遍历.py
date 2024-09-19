# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root):
        """
        递归法
        """
        self._preorderTraversal(root)
        return self.res

    def _preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return 0
        print(root.val)
        self.res.append(root.val)
        left_height = self._preorderTraversal(root.left)
        right_height = self._preorderTraversal(root.right)

    def pre_order_traversal(self, root):
        """
        迭代法
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(Solution().preorderTraversal(root))
    print(Solution().pre_order_traversal(root))
