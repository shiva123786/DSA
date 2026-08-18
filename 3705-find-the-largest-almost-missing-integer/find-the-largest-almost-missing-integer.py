class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        c=Counter(nums)
        if k==1:
            return max((x for x in nums if c[x]==1),default=-1)
        if k==n:
            return max(nums)
        return max(nums[0] if c[nums[0]]==1 else -1,nums[-1] if c[nums[-1]]==1 else -1)