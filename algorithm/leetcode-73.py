class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        cols = []
        rows = []

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for row in rows:
            matrix[row] = [0 for i in range(n)]
        for col in cols:
            for i in range(m):
                matrix[i][col] = 0
        return matrix

solution = Solution()
input = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
print(solution.setZeroes(input))
input = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print(solution.setZeroes(input))

input = [
  [1,1,1],
  [1,0,1]
]
print(solution.setZeroes(input))

input = [
  [1,0,1],
  [1,0,1]
]
print(solution.setZeroes(input))

input = [
  [1],
  [0]
]
print(solution.setZeroes(input))
input = [
  [1]
]
print(solution.setZeroes(input))
input = [
  [0]
]
print(solution.setZeroes(input))
input = [
  [0,1]
]
print(solution.setZeroes(input))
input = [

]
print(solution.setZeroes(input))

