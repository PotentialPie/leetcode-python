# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(node, min_n, max_n):
            if not node:
                return True

            if node.val <= min_n or node.val >= max_n:
                return False

            a = check(node.right, node.val, max_n)
            b = check(node.left, min_n, node.val)

            return a and b

        if not root:
            return True
        return check(root, -9999999999, 9999999999)