from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    """
    二叉树

    层序遍历 https://www.hello-algo.com/chapter_tree/binary_tree_traversal/#721
    题解 https://leetcode.cn/problems/symmetric-tree/?envType=study-plan-v2&envId=top-100-liked
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque()
        queue.append((root, root))
        while queue:
            left, right = queue.popleft()

            if not left and not right:
                continue

            if not left or not right:
                return False

            print(left.val, right.val)
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True


if __name__ == '__main__':
    # [1,2,2,null,3,null,3]
    root1 = TreeNode(1)
    root2left = TreeNode(2)
    root2right = TreeNode(2)
    root1.left = root2left
    root1.right = root2right
    # root2left.left = TreeNode(3)
    root2left.right = TreeNode(3)
    # root2right.left = TreeNode(4)
    root2right.right = TreeNode(3)

    s = Solution()
    print(s.isSymmetric(root1))
