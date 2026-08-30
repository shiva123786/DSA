class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        mod=10**9+7
        ans=0
        for n in nums:
            w=n%10
            s=str(n//10)
            x=int(s[:w])
            y=int(s[w:])
            ans=(ans+pow(x,y,mod))%mod
        return ans
        