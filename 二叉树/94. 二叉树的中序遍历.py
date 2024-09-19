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
        递归法
        """
        self._inorderTraversal(root)
        return self.res

    def _inorderTraversal(self, root):
        if not root:
            return None
        self._inorderTraversal(root.left)
        self.res.append(root.val)
        self._inorderTraversal(root.right)

    def in_order_traversal(self, root):
        """
        迭代法
        """
        if not root:
            return []

        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)

            cur = cur.right

        return res


if __name__ == '__main__':
    s = Solution()
    # root = TreeNode(1)
    # c1_right = TreeNode(2)
    # c2_left = TreeNode(3)
    # root.right = c1_right
    # c1_right.left = c2_left
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(s.inorderTraversal(root))
    print(s.in_order_traversal(root))
