class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        c=Counter()
        left=0
        sol=0
        for i in range(len(s)):
            c[s[i]]+=1
            while c[s[i]]>2:
                c[s[left]]-=1
                left+=1
            sol=max(sol,i-left+1)
        return sol