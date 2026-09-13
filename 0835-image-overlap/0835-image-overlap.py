class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        a=[(i,j) for i in range(n) for j in range(n) if img1[i][j]]
        b=[(i,j) for i in range(n) for j in range(n) if img2[i][j]]
        c=Counter((x1-x2,y1-y2) for x1,y1 in a for x2,y2 in b)
        return max(c.values(),default=0)