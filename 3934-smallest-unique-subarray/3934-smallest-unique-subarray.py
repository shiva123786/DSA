class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        mod=10**9+7
        base=911382323
        n=len(nums)
        p=[1]*(n+1)
        h=[0]*(n+1)
        for i,x in enumerate(nums):
            p[i+1]=p[i]*base%mod
            h[i+1]=(h[i]*base+x)%mod
        def array(m):
            c={}
            for i in range(n-m+1):
                x=(h[i+m]-h[i]*p[m])%mod
                c[x]=c.get(x,0)+1
            return any(v==1 for v in c.values())
        l,r=1,n
        while l<r:
            mid=(l+r)//2
            if array(mid):
                r=mid
            else:
                l=mid+1
        return l
        