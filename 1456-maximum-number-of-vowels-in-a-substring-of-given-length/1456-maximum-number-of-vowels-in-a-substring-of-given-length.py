class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v="aeiou"
        cnt=sum(c in v for c in s[:k])
        ans=cnt
        for i in range(k,len(s)):
            cnt+=(s[i] in v)-(s[i-k] in v)
            ans=max(ans,cnt)
        return ans