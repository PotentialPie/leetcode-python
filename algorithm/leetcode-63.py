# coding=utf-8
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        df = [[0 for i in range(n)] for j in range(m)]

        # 这两个边界，有问题吧啊
        if obstacleGrid[0][0] == 1:
            return 0

        # 这两个边界，有问题吧啊
        if obstacleGrid[m-1][n-1] == 1:
            return 0

        df[0][0] = 1

        # def DFS(i, j):
        #     if obstacleGrid[i][j] == 1:
        #         return df[i][j]
        #     if df[i][j] > 0:
        #         return df[i][j]
        #     else:
        #         a = 0
        #         b = 0
        #         if i-1 >= 0:
        #             a = DFS(i-1,j)
        #         if j - 1 >= 0:
        #             b = DFS(i,j-1)
        #         df[i][j] = a + b
        #         return df[i][j]
        #
        # DFS(m-1, n-1)

        for i in range(m):
            for j in range(n):
                if (i == 0  and j == 0) or obstacleGrid[i][j] == 1:
                    pass
                else:
                    a = 0
                    b = 0
                    if i - 1 >= 0:
                        a = df[i-1][j]
                    if j - 1 >= 0:
                        b = df[i][j-1]
                    df[i][j] = a + b

        return df[m-1][n-1]








solution = Solution()
input = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]
print(solution.uniquePathsWithObstacles(input))
input = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(solution.uniquePathsWithObstacles(input))

input = [
  [0,1,0],
  [0,1,0],
  [0,0,0]
]
print(solution.uniquePathsWithObstacles(input))
input = [
  [1]
]
print(solution.uniquePathsWithObstacles(input))
input = [
  [0,0]
]
print(solution.uniquePathsWithObstacles(input))
input = [
  [0,1,0]
]
print(solution.uniquePathsWithObstacles(input))
input = [
  [0,1,0],
  [0,1,0],
  [0,1,0]
]
print(solution.uniquePathsWithObstacles(input))
input = [
  [0,0,0],
  [0,1,0],
  [0,1,0]
]
print(solution.uniquePathsWithObstacles(input))
input = [[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0],[1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1],[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1],[1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]]
print(solution.uniquePathsWithObstacles(input))