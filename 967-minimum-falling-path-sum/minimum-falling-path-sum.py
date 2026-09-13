class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        dp=matrix[0][:]
        for i in range(1,n):
            ndp=[0]*n
            for j in range(n):
                ndp[j]=matrix[i][j]+min(dp[max(0,j-1):min(n,j+2)])
            dp=ndp
        return min(dp)