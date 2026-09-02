class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol=[1]*len(nums)
        p=1
        for i in range(len(nums)):
            sol[i]=p
            p*=nums[i]
        p=1
        for i in range(len(nums)-1,-1,-1):
            sol[i]*=p
            p*=nums[i]
        return sol