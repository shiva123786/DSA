class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        suffix=[0]*(n+1)
        for i in range(n-1,-1,-1):
            suffix[i]=suffix[i+1]+piles[i]
        dp={}
        def solve(i,m):
            if i==n:
                return 0
            if (i,m) in dp:
                return dp[i,m]
            best=0
            for x in range(1,min(2*m,n-i)+1):
                best=max(best,suffix[i]-solve(i+x,max(m,x)))
            dp[i,m]=best
            return best
        return solve(0,1)