class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque()
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        minutes=0
        while q and fresh:
            for _ in range(len(q)):
                r,c=q.popleft()
                for x,y in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                    if 0<=x<m and 0<=y<n and grid[x][y]==1:
                        grid[x][y]=2
                        fresh-=1
                        q.append((x,y))
            minutes+=1
        return minutes if fresh==0 else -1