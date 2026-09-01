from collections import deque,defaultdict
from itertools import product

class Solution:
    def minMoves(self,classroom,energy):
        m,n,trash=len(classroom),len(classroom[0]),0
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        visited=defaultdict(int)
        grid=[list(row) for row in classroom]

        for row,col in product(range(m),range(n)):
            if grid[row][col]=="L":
                grid[row][col]=str(trash)
                trash+=1
            if grid[row][col]=="S":
                queue=deque([(row,col,energy,0,0)])
                visited[(row,col,0)]=energy

        if trash==0:
            return 0

        while queue:
            row,col,fuel,mask,moves=queue.pop()
            moves+=1

            for dr,dc in dirs:
                r,c=row+dr,col+dc

                if r<0 or r>=m or c<0 or c>=n or grid[r][c]=="X":
                    continue

                if grid[r][c]=="R":
                    nxtFuel=energy
                else:
                    nxtFuel=fuel-1

                if nxtFuel<0:
                    continue

                nxtMask=mask

                if grid[r][c].isnumeric():
                    nxtMask|=1<<int(grid[r][c])

                    if nxtMask.bit_count()==trash:
                        return moves

                state=(r,c,nxtMask)

                if visited[state]<nxtFuel:
                    visited[state]=nxtFuel
                    queue.appendleft((r,c,nxtFuel,nxtMask,moves))

        return -1