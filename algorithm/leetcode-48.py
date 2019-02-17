# coding=utf-8
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N // 2):
            # 矩阵问题，显然边界有问题，要考虑结束的边界
            for j in range(i, len(matrix) - 1 - i):
                next_i = j
                next_j = N - 1 - i
                tmp = matrix[next_i][next_j]
                matrix[next_i][next_j] = matrix[i][j]
                matrix[i][j] = tmp
                next_i = N - 1 - i
                next_j = N - 1 - j
                tmp = matrix[next_i][next_j]
                matrix[next_i][next_j] = matrix[i][j]
                matrix[i][j] = tmp
                next_i = N - 1 - j
                next_j = i
                tmp = matrix[next_i][next_j]
                matrix[next_i][next_j] = matrix[i][j]
                matrix[i][j] = tmp
                for k in range(N):
                    print(matrix[k])
                print()
        for i in range(N):
            print(matrix[i])

solution = Solution()
#print(solution.permuteUnique([1,2,3]))
# print(solution.permuteUnique([1,1,2]))
input_matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
print(solution.rotate(input_matrix))