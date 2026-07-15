from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.solutions = []
        self.x = [-1] * n
        self.n = n
        self.n_queens_recursive(0)
        return self.solutions

    def n_queens_recursive(self, k: int):
        for i in range(self.n):
            if self.is_safe_to_place(k, i):
                self.x[k] = i
                if k == self.n - 1:
                    self.solutions.append(self.format_board())
                else:
                    self.n_queens_recursive(k + 1)

    def is_safe_to_place(self, k: int, i: int) -> bool:
        for j in range(k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(k - j):
                return False
        return True

    def format_board(self) -> List[str]:
        board = []
        for i in range(self.n):
            row_list = ["."] * self.n
            row_list[self.x[i]] = "Q"
            board.append("".join(row_list))
        return board