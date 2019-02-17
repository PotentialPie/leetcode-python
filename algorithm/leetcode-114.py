# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        stack = [root]
        last_node = TreeNode(-1)
        ## 不能理解的是：顺序问题，这个要好好琢磨琢磨
        while stack:
            node = stack.pop()
            last_node.right = node
            last_node.left = None
            if node and node.right:
                stack.append(node.right)
            if node and node.left:
                stack.append(node.left)
            last_node = node

#         if not root:
#             return root

#         def search_bottom_right(root):
#             if not root.right:
#                 return root
#             return search_bottom_right(root.right)

#         def search_up_left(root):
#             if root.left:
#                 return root
#             if root.right:
#                 return search_up_left(root.right)
#             return None

#         p, q, l = root, search_bottom_right(root), search_up_left(root)

#         while l:
#             q.right = l.left
#             l.left = None
#             l = search_up_left(l)
#             q = search_bottom_right(q)

