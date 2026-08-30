class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        INF=10**9
        dp=[INF]*(sum+1)
        dp[0]=0

        for x in nums:
            a={0:0}
            v=x;c=0
            while v<=sum:
                a[v]=c
                v*=2;c+=1
            v=x;c=1
            while v:
                a.setdefault(v//2,c)
                v//=2;c+=1

            ndp=dp[:]
            for s in range(sum+1):
                if dp[s]<INF:
                    for v,c in a.items():
                        if s+v<=sum:
                            ndp[s+v]=min(ndp[s+v],dp[s]+c)
            dp=ndp

        return -1 if dp[sum]==INF else dp[sum]