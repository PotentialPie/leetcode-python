# coding=utf-8
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result_list = []
        if not matrix:
            return result_list
        m = len(matrix)
        n = len(matrix[0])
        # # 空边界，我怎么老是忘记啊！！！！！！
        # if n == 0 or m == 0:
        #     return result_list
        # #print(m,n)
        num_spiral = min(m, n) // 2
        for i in range(num_spiral):
            for j in range(i, n - i):
                result_list.append(matrix[i][j])
            #print(result_list)
            for j in range(i + 1, m - i):
                result_list.append(matrix[j][n - 1 - i])
            print(result_list)
            for j in range(n - i - 2, i - 1, -1):
                #print(n - 1 - i, j)
                result_list.append(matrix[m - 1 - i][j])
            #print(result_list)
            for j in range(m - i - 2, i, -1):
                result_list.append(matrix[j][i])
            #print(result_list)
        if m <= n and m % 2 != 0:
            for i in range(num_spiral, n - num_spiral):
                result_list.append(matrix[num_spiral][i])
        if m > n and n % 2 != 0:
            for i in range(num_spiral, m - num_spiral):
                result_list.append(matrix[i][num_spiral])

        return result_list

solution = Solution()
print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(solution.spiralOrder([]))