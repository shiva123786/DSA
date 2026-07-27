class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        sol=0
        for i in range(n-1,-1,-1):
            if colors[i]!=colors[0]:
                sol=i
                break
        for i in range(n):
            if colors[i]!=colors[-1]:
                d=n-1-i
                if d>sol:
                    sol=d
                break
        return sol
