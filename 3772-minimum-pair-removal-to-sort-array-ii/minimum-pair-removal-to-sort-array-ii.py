class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n=len(nums)
        nums.append(inf)
        le,ri=list(range(-1,n)),list(range(1,n+1))
        h=[(a+b,i)for i,(a,b)in enumerate(pairwise(nums))]
        heapify(h)
        ans=0
        rest=n-sum(1 for a,b in pairwise(nums)if a<=b)
        while rest:
            v,i=heappop(h)
            r=ri[i]
            if le[r]!=i or nums[i]+nums[r]!=v:
                continue
            rr=ri[r]
            rest+=(nums[le[i]]<=nums[i])+(nums[i]<=nums[r])+(nums[r]<=nums[rr])
            le[rr],ri[i]=i,rr
            nums[i]=v
            rest-=1+(nums[le[i]]<=nums[i])+(nums[i]<=nums[rr])
            if i:
                heappush(h,(nums[le[i]]+nums[i],le[i]))
            if rr<n:
                heappush(h,(nums[i]+nums[rr],i))
            ans+=1
        return ans
