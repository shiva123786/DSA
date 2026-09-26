class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d=dict(knowledge)
        ans=""
        i=0
        while i<len(s):
            if s[i]=="(":
                j=s.index(")",i)
                ans+=d.get(s[i+1:j],"?")
                i=j+1
            else:
                ans+=s[i]
                i+=1
        return ans