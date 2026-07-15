class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        ans=0
        n=len(heights)
        for i in range(n+1):
            cur=0 if i==n else heights[i]
            while stack and heights[stack[-1]]>cur:
                h=heights[stack.pop()]
                if not stack:
                    w=i
                else:
                    w=i-stack[-1]-1
                ans=max(ans,h*w)
            stack.append(i)
        return ans
        