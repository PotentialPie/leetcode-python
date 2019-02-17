class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        for i in range(1, n):
            grid[0][i] = grid[0][i] + grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] = grid[i][0] + grid[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[m - 1][n - 1]

solution = Solution()
input = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(solution.minPathSum(input))
input = [
  [1,3,1]
]
print(solution.minPathSum(input))
input = [
  [9]
]
print(solution.minPathSum(input))
input = [
    []
]
print(solution.minPathSum(input))
input = [
  [1,3],
  [1,5]
]
print(solution.minPathSum(input))