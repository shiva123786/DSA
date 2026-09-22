class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs=sorted(zip(nums2,nums1),reverse=True)
        h=[]
        s=ans=0
        for b,a in pairs:
            heapq.heappush(h,a)
            s+=a
            if len(h)>k:
                s-=heapq.heappop(h)
            if len(h)==k:
                ans=max(ans,s*b)
        return ans