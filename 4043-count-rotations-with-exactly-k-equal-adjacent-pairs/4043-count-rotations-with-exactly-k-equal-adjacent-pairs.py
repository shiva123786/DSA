class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        count=0
        for shift in range(n):
            roatated=s[shift:]+s[:shift]
            score=sum(1 for i in range(n-1)if roatated[i]==roatated[i+1])
            if score==k:
                count+=1
        return count