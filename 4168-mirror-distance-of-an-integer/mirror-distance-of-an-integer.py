class Solution:
    def mirrorDistance(self, n: int) -> int:
        x=n
        rev=0
        while x:
            rev=rev*10+x%10
            x//=10
        return abs(n-rev)