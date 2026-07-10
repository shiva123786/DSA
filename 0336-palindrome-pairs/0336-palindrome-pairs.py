class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d={w:i for i,w in enumerate(words)}
        ans=[]
        for i,w in enumerate(words):
            for j in range(len(w)+1):
                a,b=w[:j],w[j:]
                if a==a[::-1]:
                    r=b[::-1]
                    if r in d and d[r]!=i:
                        ans.append([d[r],i])
                if j!=len(w) and b==b[::-1]:
                    r=a[::-1]
                    if r in d and d[r]!=i:
                        ans.append([i,d[r]])
        return ans