#coding=utf-8
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        flag_block = [[[0 for k in range(9)] for j in range(3)] for i in range(3)]
        print(flag_block)
        flag_row = [[0 for j in range(9)] for i in range(9)]
        flag_col = [[0 for j in range(9)] for i in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                # 你看啊，下标从0和从1开始的区别
                # this_num = int(board[row][col])
                this_num = int(board[row][col]) - 1
                block_row = row // 3
                block_col = col // 3
                #print(row, col, block_row, block_col)
                if flag_block[block_row][block_col][this_num] != 1 and flag_row[row][this_num] != 1 and flag_col[col][
                    this_num] != 1:
                    flag_block[block_row][block_col][this_num] = 1
                    flag_row[row][this_num] = 1
                    flag_col[col][this_num] = 1
                else:
                    return False

        return True

solution = Solution()
input1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
inpunt2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(solution.isValidSudoku(input1))
print(solution.isValidSudoku(inpunt2))
