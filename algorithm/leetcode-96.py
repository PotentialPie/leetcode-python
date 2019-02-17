class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = [[0 for i in range(n+1)] for j in range(n+1)]

        def count_BST(start, end):
            #print(start,end)
            if dp[start][end] > 0:
                return dp[start][end]
            if end - start <= 1:
                dp[start][end]=1
                return dp[start][end]
            count = 0
            for i in range(start, end):
                count += count_BST(start,i)*count_BST(i + 1, end)
            dp[start][end] = count
            return dp[start][end]

        return count_BST(0,n)


solution = Solution()
print(solution.numTrees(1))
print(solution.numTrees(2))
print(solution.numTrees(3))
print(solution.numTrees(5))
print(solution.numTrees(19))