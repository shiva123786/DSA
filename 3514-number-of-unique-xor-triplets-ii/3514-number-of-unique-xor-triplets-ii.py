class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1
        pairs=set()
        for i in range(n):
            for j in range(i+1,n):
                pairs.add(nums[i]^nums[j])
        sol=set()
        for x in pairs:
            for num in nums:
                sol.add(x^num)
        return len(sol)

        