class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def dfs_gen(left, right, temp_str):
            if len(temp_str) == 2*n:
                ans.append(temp_str)
            if left < n:
                dfs_gen(left+1, right, temp_str+'(')
            if right < left:
                dfs_gen(left, right+1, temp_str+')')
        dfs_gen(0, 0, '')
        return ans

solution = Solution()
print(solution.generateParenthesis(0))
print(solution.generateParenthesis(1))
print(solution.generateParenthesis(2))
print(solution.generateParenthesis(3))