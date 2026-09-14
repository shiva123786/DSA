class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n=len(maze),len(maze[0])
        q=deque([(entrance[0],entrance[1],0)])
        maze[entrance[0]][entrance[1]]="+"
        while q:
            r,c,d=q.popleft()
            if (r==0 or r==m-1 or c==0 or c==n-1) and d:
                return d
            for x,y in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if 0<=x<m and 0<=y<n and maze[x][y]==".":
                    maze[x][y]="+"
                    q.append((x,y,d+1))
        return -1