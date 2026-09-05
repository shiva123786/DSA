class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows=Counter(map(tuple,grid))
        cols=Counter(zip(*grid))
        return sum(rows[x]*cols[x] for x in rows)