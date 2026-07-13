class Solution:
    def decodeString(self, s: str) -> str:
        self.i=0
        def dfs():
            res=""
            num=0
            while self.i<len(s):
                if s[self.i].isdigit():
                    num=num*10+int(s[self.i])
                elif s[self.i]=="[":
                    self.i+=1
                    t=dfs()
                    res+=t*num
                    num=0
                elif s[self.i]=="]":
                    return res
                else:
                    res+=s[self.i]
                self.i+=1
            return res
        return dfs()
        