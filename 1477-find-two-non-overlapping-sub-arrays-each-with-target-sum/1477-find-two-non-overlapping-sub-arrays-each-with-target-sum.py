class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        best=[float('inf')]*(n+1)
        ans=float('inf')
        l=s=0
        for r,x in enumerate(arr):
            s+=x
            while s>target:
                s-=arr[l]
                l+=1
            if s==target:
                length=r-l+1
                if best[l]<float('inf'):
                    ans=min(ans,length+best[l])
                best[r+1]=min(best[r],length)
            else:
                best[r+1]=best[r]
        return -1 if ans==float('inf') else ans