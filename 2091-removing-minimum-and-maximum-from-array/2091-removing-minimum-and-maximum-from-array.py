class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        a=nums.index(min(nums))
        b=nums.index(max(nums))
        l=min(a,b)
        r=max(a,b)
        return min(r+1,n-l,(l+1)+(n-r))