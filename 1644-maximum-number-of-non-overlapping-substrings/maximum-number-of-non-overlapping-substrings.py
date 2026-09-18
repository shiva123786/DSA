class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first=[len(s)]*26
        last=[-1]*26
        for i,c in enumerate(s):
            x=ord(c)-97
            first[x]=min(first[x],i)
            last[x]=i
        arr=[]
        for x in range(26):
            if last[x]<0:
                continue
            l,r=first[x],last[x]
            i=l
            ok=True
            while i<=r:
                y=ord(s[i])-97
                if first[y]<l:
                    ok=False
                    break
                r=max(r,last[y])
                i+=1
            if ok:
                arr.append((r,l))
        arr.sort()
        ans=[]
        end=-1
        for r,l in arr:
            if l>end:
                ans.append(s[l:r+1])
                end=r
        return ans