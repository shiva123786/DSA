class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        inf=10**9
        dp=[inf]*(sum+1)
        dp[0]=0
        for x in nums:
            a={}
            v=x
            down=0
            while v:
                u=v
                up=0
                while u<=sum:
                    a[u]=min(a.get(u,inf),down+up)
                    u*=2
                    up+=1
                v//=2
                down+=1
            ndp=dp[:]
            for s in range(sum+1):
                if dp[s]<inf:
                    for v,c in a.items():
                        if s+v<=sum:
                            ndp[s+v]=min(ndp[s+v],dp[s]+c)
            dp=ndp


        return -1 if dp[sum]==inf else dp[sum]
        