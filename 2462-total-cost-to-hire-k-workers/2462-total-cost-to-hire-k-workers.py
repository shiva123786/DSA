class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n=len(costs)
        l=0
        r=n-1
        ans=0
        left=[]
        right=[]
        for _ in range(candidates):
            if l<=r:
                heapq.heappush(left,costs[l])
                l+=1
        for _ in range(candidates):
            if l<=r:
                heapq.heappush(right,costs[r])
                r-=1
        for _ in range(k):
            if not right or left and left[0]<=right[0]:
                ans+=heapq.heappop(left)
                if l<=r:
                    heapq.heappush(left,costs[l])
                    l+=1
            else:
                ans+=heapq.heappop(right)
                if l<=r:
                    heapq.heappush(right,costs[r])
                    r-=1
        return ans