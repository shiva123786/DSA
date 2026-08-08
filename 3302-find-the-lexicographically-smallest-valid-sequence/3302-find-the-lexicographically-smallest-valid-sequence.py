class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n=len(word1)
        m=len(word2)
        sol=[0]*(n+1)
        j=m-1
        for i in range(n-1,-1,-1):
            if j>=0 and word1[i]==word2[j]:
                j-=1
            sol[i]=m-1-j
        ans=[]
        j=0
        changed=False
        for i in range(n):
            if j==m:
                break
            if word1[i]==word2[j]:
                ans.append(i)
                j+=1
            elif not changed and sol[i+1]>=m-j-1:
                ans.append(i)
                j+=1
                changed=True
        return ans if len(ans)==m else []