# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        stack = []
        stack.append([root, 1])

        while stack:
            ## append和pop()是用来模拟栈的，栈可以用来深度优先遍历。
            ## 想要模拟队列，得用pop(0)，队列可以用来广度优先遍历
            node = stack.pop(0)
            # print(node[0].val)
            if not node[0].left and not node[0].right:
                return node[1]
            if node[0].left:
                stack.append([node[0].left, node[1] + 1])
            if node[0].right:
                stack.append([node[0].right, node[1] + 1])
            # print(stack)

