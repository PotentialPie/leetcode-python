# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        out = []
        if not root:
            return out

        def DFS(root, depth):
            if depth > len(out):
                out.append([root.val])
            else:
                out[depth - 1].append(root.val)
            if root.left:
                DFS(root.left, depth + 1)
            if root.right:
                DFS(root.right, depth + 1)

        DFS(root, 1)

        for i in range(1, len(out), 2):
            out[i].reverse()

        return out

