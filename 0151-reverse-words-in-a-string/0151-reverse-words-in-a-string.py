class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s)
        n=len(s)
        i=0
        words=[]
        while i<n:
            while i<n and s[i]==' ':
                i+=1
            if i>=n:
                break
            j=i
            while j<n and s[j]!=' ':
                j+=1
            words.append(''.join(s[i:j]))
            i=j
        return ' '.join(words[::-1])