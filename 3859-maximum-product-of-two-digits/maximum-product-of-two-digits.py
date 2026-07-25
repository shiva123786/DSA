class Solution:
    def maxProduct(self, n: int) -> int:
        f=0 
        s=0
        while n>0:
            digit=n%10
            n//=10
            if digit>f:
                s=f
                f=digit
            elif digit>s:
                s=digit
        return f*s
