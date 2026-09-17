class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp=[0]*(n+1)
        ans=0
        for i in range(1,m+1):
            prev=0
            for j in range(1,n+1):
                x=dp[j]
                if matrix[i-1][j-1]=="1":
                    dp[j]=1+min(dp[j],dp[j-1],prev)
                    ans=max(ans,dp[j])
                else:
                    dp[j]=0
                prev=x
        return ans*ans