class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def printNode(self,node):
        print(node.val)
        if node.left is not None:
            self.printNode(node.left)
        if node.right is not None:
            self.printNode(node.right)
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate(arr):
            ans = []
            for i in range(len(arr)):
                lefts, rights = generate(arr[:i]), generate(arr[i + 1:])
                for l in lefts:
                    for r in rights:
                        root, root.left, root.right = TreeNode(arr[i]), l, r
                        ans.append(root)
            #print(ans)
            return ans or [None]

        return (generate(list(range(1, n + 1)))) if n else []

solution = Solution()
for i in solution.generateTrees(3):
    solution.printNode(i)
    print()