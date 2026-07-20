class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check(a,b):
            i=j=0
            while i<len(a) and j<len(b):
                if a[i]!=b[j]:
                    return False
                c1=c2=1
                while i+1<len(a) and a[i]==a[i+1]:
                    c1+=1
                    i+=1
                while j+1<len(b) and b[j]==b[j+1]:
                    c2+=1
                    j+=1
                if c1<c2:
                    return False
                if c1!=c2 and c1<3:
                    return False
                i+=1
                j+=1
            return i==len(a) and j==len(b)
        ans=0
        for w in words:
            if check(s,w):
                ans+=1
        return ans