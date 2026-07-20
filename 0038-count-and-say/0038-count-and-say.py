class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"
        for _ in range(n-1):
            t=""
            i=0
            while  i<len(s):
                c=1
                while i+1<len(s) and s[i]==s[i+1]:
                    c+=1
                    i+=1
                t+=str(c)+s[i]
                i+=1
            s=t
        return s
                
        