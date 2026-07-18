class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        sol=float("inf")
        for i in range(n):
            if words[i]==target:
                d=abs(i-startIndex)
                sol=min(sol,n-d,d)
        return -1 if sol==float("inf") else sol
            
