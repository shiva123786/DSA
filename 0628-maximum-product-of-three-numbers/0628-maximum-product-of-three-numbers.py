class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a=-float('inf')
        b=-float('inf')
        c=-float('inf')
        x=float('inf')
        y=float('inf')
        for n in nums:
            if n>a:
                c=b
                b=a
                a=n
            elif n>b:
                c=b
                b=n
            elif n>c:
                c=n
            if n<x:
                y=x
                x=n
            elif n<y:
                y=n

        p1=a*b*c
        p2=x*y*a
        return p1 if p1>p2 else p2