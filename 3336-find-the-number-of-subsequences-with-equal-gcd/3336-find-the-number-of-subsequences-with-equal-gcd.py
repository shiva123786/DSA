class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod=10**9+7
        m=max(nums)
        dp={(0,0):1}
        for x in nums:
            ndp=dp.copy()
            for (a,b),v in dp.items():
                na=gcd(a,x)
                nb=gcd(b,x)
                ndp[(na,b)]=(ndp.get((na,b),0)+v)%mod
                ndp[(a,nb)]=(ndp.get((a,nb),0)+v)
            dp=ndp
        ans=0
        for (a,b),v in dp.items():
            if a==b and a:
                ans=(ans+v)%mod
        return ans