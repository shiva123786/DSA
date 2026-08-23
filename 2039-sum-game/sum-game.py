class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        cnt1=cnt2=s1=s2=0
        for i,c in enumerate(num):
            if i<n//2:
                if c=="?":
                    cnt1+=1
                else:
                    s1+=int(c)
            else:
                if c=="?":
                    cnt2+=1
                else:
                    s2+=int(c)
        return (cnt1+cnt2)%2==1 or 2*(s1-s2)!=9*(cnt2-cnt1)