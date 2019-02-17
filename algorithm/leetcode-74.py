class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n - 1

        while start <= end:
            middle = (start + end) // 2

            row = middle // n
            col = middle % n
            #print(row,col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = middle - 1
            else:
                start = middle + 1
        return False

solution = Solution()
input = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(solution.searchMatrix(input,3))
input = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(solution.searchMatrix(input,13))
input = [
]
print(solution.searchMatrix(input,13))
input = [
    [13]
]
print(solution.searchMatrix(input,13))
input = [
    [1,13,26]
]
print(solution.searchMatrix(input,13))
input = [
    [1],
    [13],
    [26]
]
print(solution.searchMatrix(input,13))