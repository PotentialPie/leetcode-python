# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        traversal_list = []
        if not root:
            return traversal_list

        def DFS(root, depth):
            if len(traversal_list) <= depth - 1:
                traversal_list.append([root.val])
            else:
                traversal_list[depth - 1].append(root.val)
            if root.left:
                DFS(root.left, depth + 1)
            if root.right:
                DFS(root.right, depth + 1)

        DFS(root, 1)
        return traversal_list

