class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans=0
        for i in range(1,n+1):
            x=i
            good=False
            while x:
                d=x%10
                if d in [3,4,7]:
                    good=False
                    break
                if d in [2,5,6,9]:
                    good=True
                x//=10
            else:
                if good:
                    ans+=1
        return ans
        