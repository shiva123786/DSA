from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)
    def find_best_empty(self, board):
        best_pos = None
        min_options = 10
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    options = 0
                    for i in range(1, 10):
                        if self.is_valid(board, str(i), (r, c)):
                            options += 1
                    if options < min_options:
                        min_options = options
                        best_pos = (r, c)
                        if min_options == 1:
                            return best_pos
        return best_pos

    def solve(self, board):
        find = self.find_best_empty(board)        
        if not find:
            return True  
        else:
            row, col = find
        for i in range(1, 10):
            num_str = str(i)
            if self.is_valid(board, num_str, (row, col)):
                board[row][col] = num_str
                if self.solve(board):
                    return True
                board[row][col] = "." 
        return False

    def is_valid(self, board, num_str, pos):
        row, col = pos
        # Check Row
        for i in range(9):
            if board[row][i] == num_str:
                return False
        # Check Column
        for i in range(9):
            if board[i][col] == num_str:
                return False
        # Check 3x3 box
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num_str:
                    return False
        return True