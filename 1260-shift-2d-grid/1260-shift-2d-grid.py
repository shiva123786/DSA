class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        arr=[]
        for row in grid:
            arr.extend(row)
        k%=m*n
        arr=arr[-k:]+arr[:-k]
        ans=[]
        for i in range(0,m*n,n):
            ans.append(arr[i:i+n])
        return ans
        