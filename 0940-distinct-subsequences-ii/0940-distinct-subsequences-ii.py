class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod=10**9+7
        dp=[0]*26
        for c in s:
            x=ord(c)-97
            dp[x]=(sum(dp)+1)%mod
        return sum(dp)%mod