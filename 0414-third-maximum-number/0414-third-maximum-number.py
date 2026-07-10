class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=b=c=float("-inf")
        for x in nums:
            if x==a or x==b or x==c:
                continue
            if x>a:
                c=b
                b=a
                a=x
            elif x>b:
                c=b
                b=x
            elif x>c:
                c=x
        return a if c==float("-inf") else c
