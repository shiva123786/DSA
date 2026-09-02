class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans=0
        arrow=float('-inf')
        for s,e in points:
            if s>arrow:
                ans+=1
                arrow=e
        return ans