from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """
    二叉树
    题解：层序遍历，然后返回每层的最后一个值
    """

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
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
            res.append(vals[-1])
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # root.left.right.right = TreeNode(15)
    # root.right.right = TreeNode(7)
    # root.right.right = TreeNode(7)
    print(Solution().rightSideView(root))
