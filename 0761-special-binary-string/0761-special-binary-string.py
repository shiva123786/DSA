class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s)<=2:
            return s
        ans=[]
        bal=0
        start=0
        for i,c in enumerate(s):
            if c=="1":
                bal+=1
            else:
                bal-=1
            if bal==0:
                ans.append("1"+self.makeLargestSpecial(s[start+1:i])+"0")
                start=i+1
        ans.sort(reverse=True)
        return "".join(ans)