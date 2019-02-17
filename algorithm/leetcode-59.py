class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []

        spiral_num = n // 2
        spiral_matrix = [[0 for j in range(n)] for i in range(n)]
        index = 1
        for i in range(spiral_num):
            for k in range(i, n - i):
                spiral_matrix[i][k] = index
                index = index + 1
            for k in range(i + 1, n - i):
                spiral_matrix[k][n - i - 1] = index
                index = index + 1
            for k in range(n - i - 2, i - 1, -1):
                spiral_matrix[n - i - 1][k] = index
                index = index + 1
            for k in range(n - i - 2, i, -1):
                spiral_matrix[k][i] = index
                index = index + 1
        if n % 2 != 0:
            spiral_matrix[spiral_num][spiral_num] = index
        return spiral_matrix

solution = Solution()
print(solution.generateMatrix(-1))
print(solution.generateMatrix(0))
print(solution.generateMatrix(1))
print(solution.generateMatrix(2))
print(solution.generateMatrix(3))
print(solution.generateMatrix(4))
print(solution.generateMatrix(5))