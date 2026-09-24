class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        t=[]
        ans=[]
        for x in obstacles:
            i=bisect_right(t,x)
            ans.append(i+1)
            if i==len(t):
                t.append(x)
            else:
                t[i]=x
        return ans