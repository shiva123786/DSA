class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(x):
            r=0
            while x:
                r=r*10+x%10
                x//=10
            return r
        pos={}
        ans=float("inf")
        for i,x in enumerate(nums):
            if x in pos:
                ans=min(ans,(i-pos[x]))
            pos[rev(x)]=i
        return -1 if ans==float("inf") else ans
