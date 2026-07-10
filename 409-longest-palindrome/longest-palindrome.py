class Solution:
    def longestPalindrome(self, s: str) -> int:
        c={}
        for x in s:
            c[x]=c.get(x,0)+1
        ans=0
        odd=False
        for v in c.values():
            ans+=v//2*2
            if v%2:
                odd=True
        return ans+odd