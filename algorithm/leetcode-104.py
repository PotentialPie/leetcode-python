# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        max_depth = [1]

        def DFS(root, depth):
            if not root.left and not root.right:
                max_depth[0] = max(max_depth[0], depth)
                return

            if root.left:
                DFS(root.left, depth + 1)
            if root.right:
                DFS(root.right, depth + 1)

        DFS(root, 1)

        return max_depth[0]
