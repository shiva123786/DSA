class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        c=Counter()
        l=0
        sol=0
        for i in range(len(nums)):
            c[nums[i]]+=1
            while c[nums[i]]>k:
                c[nums[l]]-=1
                l+=1
            sol=max(sol,i-l+1)
        return sol