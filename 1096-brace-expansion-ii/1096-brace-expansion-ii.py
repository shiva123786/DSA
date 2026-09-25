class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            cur={""}
            res=set()
            while i<len(expression) and expression[i]!="}":
                if expression[i]==",":
                    res|=cur
                    cur={""}
                    i+=1
                elif expression[i]=="{":
                    sub,i=parse(i+1)
                    cur={a+b for a in cur for b in sub}
                    i+=1
                else:
                    cur={a+expression[i] for a in cur}
                    i+=1
            return res|cur,i
        return sorted(parse(0)[0])