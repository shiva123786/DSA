class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        temp = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                new_col = (j - rowShift[i]) % n
                temp[i][new_col] = grid[i][j]

        result = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                new_row = (i - colShift[j]) % n
                result[new_row][j] = temp[i][j]

        return result